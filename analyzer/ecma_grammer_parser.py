import ply.lex as lex
import ply.yacc as yacc

test_data = 'ArgumentList[Yield, Await] : ArgumentList[?Yield, ?Await] `,` `...` AssignmentExpression[+In, ?Yield, ?Await]'

tokens = (
	'ID',
	'TEXT',
	'PLUS',
	'NEGATION',
	'COLON',
	'COMMA',
	'QUESTIONMARK',
	'LSQUREBUCKET',
	'RSQUREBUCKET',
	'IGNORECHARACTERS'
)

t_ignore = ' \t'

t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_TEXT = r'`[^`]*`'
t_PLUS = r'\+'
t_NEGATION = r'~'
t_COLON = r':'
t_COMMA = r','
t_QUESTIONMARK = r'\?'
t_LSQUREBUCKET = r'\['
t_RSQUREBUCKET = r'\]'
t_IGNORECHARACTERS = r'\#.*'

def t_error(t):
	raise(Exception("Illegal character '%s'" % t.value[0]))

"""
RULE : RULENAME : RULENODES
RULENAME : ID
		 | ID PARAM
PARAM : [ PARAMIDS ]
PARAMIDS : PARAMID
		 | PARAMID, PARAMIDS
PARAMID: ID
		 | COMMA ID
		 | ? ID
		 | ~ ID
RULENODES : RULENODE
		  | RULENODES RULENODE
RULENODE : TEXTNODE
		 | NAMENONE 
TEXTNODE : TEXT
		 | TEXT QUESTIONMARK
NAMENONE : RULENAME
		 | RULENAME QUESTIONMARK
"""
def p_rule(p):
	"""
	RULE : RULENAME COLON RULENODES
		 | RULENAME COLON PARAM RULENODES
		 | RULENAME COLON RULENODES IGNORECHARACTERS
		 | RULENAME COLON PARAM RULENODES IGNORECHARACTERS
	"""
	rule = {}
	rule['name'] = p[1]['ID']
	rule['arguments'] = p[1]['attributes']
	rule['nodes'] = []
	rule['constraints'] = []

	if len(p) == 4:
		rule['nodes'] = p[3]
	elif len(p) == 5:
		if isinstance(p[3], list) and isinstance(p[4], list):
			rule['nodes'] = p[4]
			rule['constraints'] = p[3]
		else:
			rule['nodes'] = p[3]
	elif len(p) == 6:
		rule['nodes'] = p[4]
		rule['constraints'] = p[3]

	p[0] = rule

def p_name(p):
	"""
	RULENAME : ID
			 | ID PARAM
	"""
	name = {}
	name['ID'] = p[1]
	name['attributes'] = []
	if len(p) == 3:
		name['attributes'] = p[2]
	p[0] = name

def p_param(p):
	""" PARAM : LSQUREBUCKET PARAMIDS RSQUREBUCKET """
	p[0] = p[2]

def p_paramids(p):
	"""
	PARAMIDS : PARAMID
			 | PARAMIDS COMMA PARAMID
	"""
	ids = []
	if len(p) == 2:
		ids.append(p[1])
	elif len(p) ==4 :
		ids.extend(p[1])
		ids.append(p[3])
	p[0] = ids

def p_paramid(p):
	"""
	PARAMID : ID
			| PLUS ID
			| NEGATION ID
			| QUESTIONMARK ID
	"""
	ID = ''
	if len(p)==2:
		ID = p[1]
	elif len(p)==3:
		ID = p[1]+p[2]
	
	p[0] = ID

def p_rulenodes(p):
	"""
	RULENODES : RULENODE
			  | RULENODES RULENODE
	"""
	nodes = []
	if len(p) == 2:
		nodes.append(p[1])
	else:
		nodes.extend(p[1])
		nodes.append(p[2])
	p[0] = nodes

def p_rulenode(p):
	"""
	RULENODE : TEXTNODE
			 | NAMENONE
	"""
	p[0] = p[1]

def p_textnode(p):
	"""
	TEXTNODE : TEXT
			 | TEXT QUESTIONMARK
	"""
	node = {}
	node['type'] = 'TEXTNODE'
	node['value'] = p[1]
	node['optional'] = False
	node['attributes'] = []

	if len(p) == 3:
		node['optional'] = True
	p[0] = node

def p_namenode(p):
	"""
	NAMENONE : RULENAME
			 | RULENAME QUESTIONMARK
	"""
	node = {}
	node['type'] = 'NAMENODE'
	node['value'] = p[1]['ID']
	node['optional'] = False
	node['attributes'] = p[1]['attributes']

	if len(p) == 3:
		node['optional'] = True
	p[0] = node

def p_error(p):
	raise(Exception("rule error at %s" % p))
#lexer = lex.lex()
#lexer.input(test_data)

#for tok in lexer:
#	print(tok)

lex.lex()
parser = yacc.yacc()

def parse(text):
	print('[parse] %s' % text)
	ast = parser.parse(text)
	ast['text'] = text
	#print('[parse] %s' % str(ast))
	return ast

