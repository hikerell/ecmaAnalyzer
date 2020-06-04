import os, sys
import re
import copy

import ecma_grammer_parser 

class Translator(object):
    """docstring for Translator"""
    def __init__(self):
        super(Translator, self).__init__()

    def loadfile(self, in_file, out_file):
        with open(in_file) as fr:
            text = fr.read()
            self.loadtext(text, out_file)

    def loadtext(self, text, out_file):
        fw = open(out_file, 'w')
        fw.write('from language import Builder' + '\n')
        fw.write('from language import Stage' + '\n')
        fw.write('from language import State' + '\n')
        fw.write('builder = Builder.get_builder()' + '\n')
        fw.write('\n')

        splits = text.split('\n')
        lines = [line.strip() for line in splits if line.strip()]
        rules = self.parse(lines)
        for rule in rules:
            trans_rules = self.translate(rule)
            for trans_rule in trans_rules:
                s = self.makeup(trans_rule)
                #filter yield and waait rules
                #if '_Yield' in s or '_Await' in s:
                #   continue
                data = '#' + rule['text'] + '\n'
                data += s + '\n'
                data += 'def _(context, ruler, stage=Stage.Prepare, target=\'\', storage={ }): pass' + '\n'
                data += '\n'
                fw.write(data)
                print(data)
        fw.close()

    def parse(self, lines):
        rule_lines = []
        head = None
        body = None
        break_line_mode = False
        rules = []
        for line in lines:
            if line.endswith(':'):
                break_line_mode = False
                head = line[:-1]
            elif line.endswith(': one of'):
                break_line_mode = True
                head = line.split(':')[0].strip()
            else:
                if break_line_mode:
                    breaked_bodys = line.split(' ')
                    breaked_lines = ['%s : %s' % (head, body) for body in breaked_bodys]
                    #rule_lines.extend(breaked_lines)
                    for rule_line in breaked_lines:
                        rule = ecma_grammer_parser.parse(rule_line)
                        rule['text'] = '%s : one of %s' % (head, line)
                        rules.append(rule)
                else:
                    body = line
                    body = body.replace('IdentifierName but not ReservedWord', 'IdentifierName')
                    body = body.replace('[no LineTerminator here]', '')
                    body = body.replace('[no |LineTerminator| here]', '')
                    body = body.replace('[empty]', '``')
                    if 'lookahead' in body:
                        print('[lookahead]: sub ... before: %s' % body)
                        body = re.sub(r'\[lookahead[^\]]+\]', ' ', body)
                        print('[lookahead]: sub ... after: %s' % body)
                    rule_line = '%s : %s' % (head, body)
                    #rule_lines.append(rule_line)
                    
                    rule = ecma_grammer_parser.parse(rule_line)
                    rule['text'] = '%s : %s' % (head, body)
                    rules.append(rule)
        return rules

    def translate(self, rule):
        stage1_rules = self.translate_expand_name(rule)

        stage2_rules = []
        for r in stage1_rules:
            rules = self.translate_reduce_optional_node(r)
            stage2_rules.extend(rules)

        stage3_rules = []
        for r in stage2_rules:
            rules = self.translate_reduce_constraint_rule(r)
            stage3_rules.extend(rules)

        stage4_rules = []
        for r in stage3_rules:
            rules = self.translate_reduce_node_param_rule(r)
            stage4_rules.extend(rules)

        return stage4_rules

    def translate_expand_name(self, rule):
        names = [ rule['name'] ]
        arguments = list(rule['arguments'])
        while len(arguments)!=0:
            arg = arguments[0]
            new_names = []
            for name in names:
                new_names.append('%s_%s' % (name, arg))
            names.extend(new_names)
            del(arguments[0])

        #if len(names)!=1:
        #   print('[expand_name stage] rule: %s' % rule['text'])
        #   print('[expand_name stage] create %d new name' % len(names))
        #   for name in names:
        #       print('[expand_name stage]         %s ' % name)

        expand_name_rules = []
        for name in names:
            r = copy.deepcopy(rule)
            r['name'] = name
            expand_name_rules.append(r)

        return expand_name_rules

    def translate_reduce_optional_node(self, rule):
        maybe_optional_rules = [ rule ]
        no_optional_rules = []
        while len(maybe_optional_rules)!=0:
            target = maybe_optional_rules.pop()
            break_rule = False
            for idx, node in enumerate(target['nodes']):
                if not node['optional']:
                    continue
                break_rule = True
                node['optional'] = False
                new_rule = copy.deepcopy(target)
                maybe_optional_rules.append(new_rule)

                del(target['nodes'][idx])
                maybe_optional_rules.append(target)
                break

            if not break_rule:
                no_optional_rules.append(target)

        for r in no_optional_rules:
            if len(r['nodes'])==0:
                print('[optional stage] empty nodes... so add an empty TEXT node')
                node = {}
                node = {}
                node['type'] = 'TEXTNODE'
                node['value'] = '``'
                node['optional'] = False
                node['attributes'] = []
                r['nodes'].append(node)
        #if len(no_optional_rules)!=1:
        #   print('[optional stage] rule: %s' % rule['text'])
        #   print('[optional stage] create %d new rules' % len(no_optional_rules))
        #   for r in no_optional_rules:
        #       print('[optional stage]         %s ' % self.rule_format(r))

        return no_optional_rules

    def translate_reduce_constraint_rule(self, rule):
        constraints = rule['constraints']
        assert(len(constraints)<2)

        if len(constraints)==0:
            return [ rule ]

        rules = []
        constraint = constraints[0]
        op = constraint[0]
        attr = constraint[1:]

        assert(op in ['+', '~'])
        assert(attr in rule['arguments'])

        if '_%s' % attr in rule['name']:
            if op=='+':
                rules = [ rule ]
        else:
            if op=='~':
                rules = [ rule ]

        if len(rules)!=1:
            print('[constraint stage] rule: %s' % rule['text'])
            print('[constraint stage] rule was deleted')

        return rules

    def translate_reduce_node_param_rule(self, rule):
        def parse_attribute(attribute):
            op = None
            attr = None
            if attribute[0] in ['+', '?', '~']:
                op = attribute[0]
                attr = attribute[1:]
            else:
                attr = attribute
            return (op, attr)

        for node in rule['nodes']:
            if len(node['attributes'])==0:
                continue
            for attribute in node['attributes']:
                op, attr = parse_attribute(attribute)
                pattern = '_%s' % attr
                if op=='+':
                    node['value'] += pattern
                elif op=='?':
                    if pattern in rule['name']:
                        node['value'] += pattern
                elif op=='~':
                    print(rule['text'])
                    #assert(pattern in rule['name'])
                    #if (pattern in rule['name']):
                    #   whatisit()
                    pass
                else:
                    print(rule['text'])
                    whatisit()

        return [ rule ]

    def rule_format(self, rule):
        text = ''
        text += rule['name']
        
        if len(rule['arguments'])!=0:
            args = ', '.join(rule['arguments'])
            text += '[%s]' % args
        text += ' : '
        
        if len(rule['constraints'])!=0:
            text += '[%s]' % (', '.join(rule['constraints']))

        text += ' '

        for node in rule['nodes']:
            text += node['value']   
            if len(node['attributes'])!=0:
                text += '[%s]' % (', '.join(node['attributes']))
            if node['optional']:
                text += '?'
            text += ' '

        text = text.strip()
        return text

    def makeup_text(self, rule):
        text = ''
        text += rule['name']
        text += ' :'

        for node in rule['nodes']:
            text += ' '
            text += node['value']

        text = text.strip()
        return text

    def makeup(self, rule):
        text = ''
        text += rule['name']
        text += ' :'

        for node in rule['nodes']:
            text += ' '
            text += node['value']

        text = text.strip()
        text = """@builder.build('%s')""" % text
        return text

if __name__=='__main__':
    #in_file = sys.argv[1]
    #out_file = sys.argv[2]
    #t = Translator()
    #t.loadfile(in_file, out_file)

    in_file = '../ecma_2018_9_0/grammer_12_Expressions.txt'
    out_file = '../Expressions_rules.py'
    Translator().loadfile(in_file, out_file)

    in_file = '../ecma_2018_9_0/grammer_13_Statements_and_Declarations.txt'
    out_file = '../Statements_and_Declarations_rules.py'
    Translator().loadfile(in_file, out_file)

    in_file = '../ecma_2018_9_0/grammer_14_Functions_and_Classes.txt'
    out_file = '../Functions_and_Classes_rules.py'
    Translator().loadfile(in_file, out_file)
    #t = Translator()
    #rule = ecma_grammer_parser.parse('FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?')
    #rules = t.translate(rule)
    #for r in rules:
    #   print(t.makeup(r))

        