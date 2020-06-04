from language import Builder
builder = Builder.get_builder()

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration : `function` BindingIdentifier `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Yield : `function` BindingIdentifier_Yield `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Await : `function` BindingIdentifier_Await `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Yield_Await : `function` BindingIdentifier_Yield_Await `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Default : `function` BindingIdentifier `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Yield_Default : `function` BindingIdentifier_Yield `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Await_Default : `function` BindingIdentifier_Await `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Yield_Await_Default : `function` BindingIdentifier_Yield_Await `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : [+Default] `function` `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Default : `function` `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : [+Default] `function` `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Yield_Default : `function` `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : [+Default] `function` `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Await_Default : `function` `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionDeclaration[Yield, Await, Default]  : [+Default] `function` `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionDeclaration_Yield_Await_Default : `function` `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionExpression  : `function` BindingIdentifier[~Yield, ~Await]? `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionExpression : `function` `(` FormalParameters `)` `{` FunctionBody `}`')

#FunctionExpression  : `function` BindingIdentifier[~Yield, ~Await]? `(` FormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='FunctionExpression : `function` BindingIdentifier `(` FormalParameters `)` `{` FunctionBody `}`')

#UniqueFormalParameters[Yield, Await]  : FormalParameters[?Yield, ?Await]
builder.r(w=1, d='UniqueFormalParameters : FormalParameters')

#UniqueFormalParameters[Yield, Await]  : FormalParameters[?Yield, ?Await]
builder.r(w=1, d='UniqueFormalParameters_Yield : FormalParameters_Yield')

#UniqueFormalParameters[Yield, Await]  : FormalParameters[?Yield, ?Await]
builder.r(w=1, d='UniqueFormalParameters_Await : FormalParameters_Await')

#UniqueFormalParameters[Yield, Await]  : FormalParameters[?Yield, ?Await]
builder.r(w=1, d='UniqueFormalParameters_Yield_Await : FormalParameters_Yield_Await')

#FormalParameters[Yield, Await]  : ``
builder.r(w=1, d='FormalParameters : ``')

#FormalParameters[Yield, Await]  : ``
builder.r(w=1, d='FormalParameters_Yield : ``')

#FormalParameters[Yield, Await]  : ``
builder.r(w=1, d='FormalParameters_Await : ``')

#FormalParameters[Yield, Await]  : ``
builder.r(w=1, d='FormalParameters_Yield_Await : ``')

#FormalParameters[Yield, Await]  : FunctionRestParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameters : FunctionRestParameter')

#FormalParameters[Yield, Await]  : FunctionRestParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Yield : FunctionRestParameter_Yield')

#FormalParameters[Yield, Await]  : FunctionRestParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Await : FunctionRestParameter_Await')

#FormalParameters[Yield, Await]  : FunctionRestParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Yield_Await : FunctionRestParameter_Yield_Await')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await]
builder.r(w=1, d='FormalParameters : FormalParameterList')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Yield : FormalParameterList_Yield')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Await : FormalParameterList_Await')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Yield_Await : FormalParameterList_Yield_Await')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,`
builder.r(w=1, d='FormalParameters : FormalParameterList `,`')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,`
builder.r(w=1, d='FormalParameters_Yield : FormalParameterList_Yield `,`')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,`
builder.r(w=1, d='FormalParameters_Await : FormalParameterList_Await `,`')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,`
builder.r(w=1, d='FormalParameters_Yield_Await : FormalParameterList_Yield_Await `,`')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FunctionRestParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameters : FormalParameterList `,` FunctionRestParameter')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FunctionRestParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Yield : FormalParameterList_Yield `,` FunctionRestParameter_Yield')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FunctionRestParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Await : FormalParameterList_Await `,` FunctionRestParameter_Await')

#FormalParameters[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FunctionRestParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameters_Yield_Await : FormalParameterList_Yield_Await `,` FunctionRestParameter_Yield_Await')

#FormalParameterList[Yield, Await]  : FormalParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameterList : FormalParameter')

#FormalParameterList[Yield, Await]  : FormalParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameterList_Yield : FormalParameter_Yield')

#FormalParameterList[Yield, Await]  : FormalParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameterList_Await : FormalParameter_Await')

#FormalParameterList[Yield, Await]  : FormalParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameterList_Yield_Await : FormalParameter_Yield_Await')

#FormalParameterList[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FormalParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameterList : FormalParameterList `,` FormalParameter')

#FormalParameterList[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FormalParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameterList_Yield : FormalParameterList_Yield `,` FormalParameter_Yield')

#FormalParameterList[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FormalParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameterList_Await : FormalParameterList_Await `,` FormalParameter_Await')

#FormalParameterList[Yield, Await]  : FormalParameterList[?Yield, ?Await] `,` FormalParameter[?Yield, ?Await]
builder.r(w=1, d='FormalParameterList_Yield_Await : FormalParameterList_Yield_Await `,` FormalParameter_Yield_Await')

#FunctionRestParameter[Yield, Await]  : BindingRestElement[?Yield, ?Await]
builder.r(w=1, d='FunctionRestParameter : BindingRestElement')

#FunctionRestParameter[Yield, Await]  : BindingRestElement[?Yield, ?Await]
builder.r(w=1, d='FunctionRestParameter_Yield : BindingRestElement_Yield')

#FunctionRestParameter[Yield, Await]  : BindingRestElement[?Yield, ?Await]
builder.r(w=1, d='FunctionRestParameter_Await : BindingRestElement_Await')

#FunctionRestParameter[Yield, Await]  : BindingRestElement[?Yield, ?Await]
builder.r(w=1, d='FunctionRestParameter_Yield_Await : BindingRestElement_Yield_Await')

#FormalParameter[Yield, Await]  : BindingElement[?Yield, ?Await]
builder.r(w=1, d='FormalParameter : BindingElement')

#FormalParameter[Yield, Await]  : BindingElement[?Yield, ?Await]
builder.r(w=1, d='FormalParameter_Yield : BindingElement_Yield')

#FormalParameter[Yield, Await]  : BindingElement[?Yield, ?Await]
builder.r(w=1, d='FormalParameter_Await : BindingElement_Await')

#FormalParameter[Yield, Await]  : BindingElement[?Yield, ?Await]
builder.r(w=1, d='FormalParameter_Yield_Await : BindingElement_Yield_Await')

#FunctionBody[Yield, Await]  : FunctionStatementList[?Yield, ?Await]
builder.r(w=1, d='FunctionBody : FunctionStatementList')

#FunctionBody[Yield, Await]  : FunctionStatementList[?Yield, ?Await]
builder.r(w=1, d='FunctionBody_Yield : FunctionStatementList_Yield')

#FunctionBody[Yield, Await]  : FunctionStatementList[?Yield, ?Await]
builder.r(w=1, d='FunctionBody_Await : FunctionStatementList_Await')

#FunctionBody[Yield, Await]  : FunctionStatementList[?Yield, ?Await]
builder.r(w=1, d='FunctionBody_Yield_Await : FunctionStatementList_Yield_Await')

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
builder.r(w=1, d='FunctionStatementList : ``')

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
builder.r(w=1, d='FunctionStatementList : StatementList_Return')

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
builder.r(w=1, d='FunctionStatementList_Yield : ``')

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
builder.r(w=1, d='FunctionStatementList_Yield : StatementList_Yield_Return')

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
builder.r(w=1, d='FunctionStatementList_Await : ``')

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
builder.r(w=1, d='FunctionStatementList_Await : StatementList_Await_Return')

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
builder.r(w=1, d='FunctionStatementList_Yield_Await : ``')

#FunctionStatementList[Yield, Await]  : StatementList[?Yield, ?Await, +Return]?
builder.r(w=1, d='FunctionStatementList_Yield_Await : StatementList_Yield_Await_Return')

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
builder.r(w=1, d='ArrowFunction : ArrowParameters `=>` ConciseBody')

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
builder.r(w=1, d='ArrowFunction_In : ArrowParameters `=>` ConciseBody_In')

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
builder.r(w=1, d='ArrowFunction_Yield : ArrowParameters_Yield `=>` ConciseBody')

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
builder.r(w=1, d='ArrowFunction_In_Yield : ArrowParameters_Yield `=>` ConciseBody_In')

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
builder.r(w=1, d='ArrowFunction_Await : ArrowParameters_Await `=>` ConciseBody')

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
builder.r(w=1, d='ArrowFunction_In_Await : ArrowParameters_Await `=>` ConciseBody_In')

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
builder.r(w=1, d='ArrowFunction_Yield_Await : ArrowParameters_Yield_Await `=>` ConciseBody')

#ArrowFunction[In, Yield, Await]  : ArrowParameters[?Yield, ?Await]  `=>` ConciseBody[?In]
builder.r(w=1, d='ArrowFunction_In_Yield_Await : ArrowParameters_Yield_Await `=>` ConciseBody_In')

#ArrowParameters[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
builder.r(w=1, d='ArrowParameters : BindingIdentifier')

#ArrowParameters[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
builder.r(w=1, d='ArrowParameters_Yield : BindingIdentifier_Yield')

#ArrowParameters[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
builder.r(w=1, d='ArrowParameters_Await : BindingIdentifier_Await')

#ArrowParameters[Yield, Await]  : BindingIdentifier[?Yield, ?Await]
builder.r(w=1, d='ArrowParameters_Yield_Await : BindingIdentifier_Yield_Await')

#ArrowParameters[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
builder.r(w=1, d='ArrowParameters : CoverParenthesizedExpressionAndArrowParameterList')

#ArrowParameters[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
builder.r(w=1, d='ArrowParameters_Yield : CoverParenthesizedExpressionAndArrowParameterList_Yield')

#ArrowParameters[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
builder.r(w=1, d='ArrowParameters_Await : CoverParenthesizedExpressionAndArrowParameterList_Await')

#ArrowParameters[Yield, Await]  : CoverParenthesizedExpressionAndArrowParameterList[?Yield, ?Await] #parencover
builder.r(w=1, d='ArrowParameters_Yield_Await : CoverParenthesizedExpressionAndArrowParameterList_Yield_Await')

#ConciseBody[In]  :   AssignmentExpression[?In, ~Yield, ~Await]
builder.r(w=1, d='ConciseBody : AssignmentExpression')

#ConciseBody[In]  :   AssignmentExpression[?In, ~Yield, ~Await]
builder.r(w=1, d='ConciseBody_In : AssignmentExpression_In')

#ConciseBody[In]  : `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='ConciseBody : `{` FunctionBody `}`')

#ConciseBody[In]  : `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='ConciseBody_In : `{` FunctionBody `}`')

#ArrowFormalParameters[Yield, Await]  : `(` UniqueFormalParameters[?Yield, ?Await] `)`
builder.r(w=1, d='ArrowFormalParameters : `(` UniqueFormalParameters `)`')

#ArrowFormalParameters[Yield, Await]  : `(` UniqueFormalParameters[?Yield, ?Await] `)`
builder.r(w=1, d='ArrowFormalParameters_Yield : `(` UniqueFormalParameters_Yield `)`')

#ArrowFormalParameters[Yield, Await]  : `(` UniqueFormalParameters[?Yield, ?Await] `)`
builder.r(w=1, d='ArrowFormalParameters_Await : `(` UniqueFormalParameters_Await `)`')

#ArrowFormalParameters[Yield, Await]  : `(` UniqueFormalParameters[?Yield, ?Await] `)`
builder.r(w=1, d='ArrowFormalParameters_Yield_Await : `(` UniqueFormalParameters_Yield_Await `)`')

#MethodDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition : PropertyName `(` UniqueFormalParameters `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Yield : PropertyName_Yield `(` UniqueFormalParameters `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Await : PropertyName_Await `(` UniqueFormalParameters `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, ~Await] `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Yield_Await : PropertyName_Yield_Await `(` UniqueFormalParameters `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : GeneratorMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition : GeneratorMethod')

#MethodDefinition[Yield, Await]  : GeneratorMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Yield : GeneratorMethod_Yield')

#MethodDefinition[Yield, Await]  : GeneratorMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Await : GeneratorMethod_Await')

#MethodDefinition[Yield, Await]  : GeneratorMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Yield_Await : GeneratorMethod_Yield_Await')

#MethodDefinition[Yield, Await]  : AsyncMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition : AsyncMethod')

#MethodDefinition[Yield, Await]  : AsyncMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Yield : AsyncMethod_Yield')

#MethodDefinition[Yield, Await]  : AsyncMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Await : AsyncMethod_Await')

#MethodDefinition[Yield, Await]  : AsyncMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Yield_Await : AsyncMethod_Yield_Await')

#MethodDefinition[Yield, Await]  : AsyncGeneratorMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition : AsyncGeneratorMethod')

#MethodDefinition[Yield, Await]  : AsyncGeneratorMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Yield : AsyncGeneratorMethod_Yield')

#MethodDefinition[Yield, Await]  : AsyncGeneratorMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Await : AsyncGeneratorMethod_Await')

#MethodDefinition[Yield, Await]  : AsyncGeneratorMethod[?Yield, ?Await]
builder.r(w=1, d='MethodDefinition_Yield_Await : AsyncGeneratorMethod_Yield_Await')

#MethodDefinition[Yield, Await]  : `get` PropertyName[?Yield, ?Await] `(` `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition : `get` PropertyName `(` `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : `get` PropertyName[?Yield, ?Await] `(` `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Yield : `get` PropertyName_Yield `(` `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : `get` PropertyName[?Yield, ?Await] `(` `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Await : `get` PropertyName_Await `(` `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : `get` PropertyName[?Yield, ?Await] `(` `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Yield_Await : `get` PropertyName_Yield_Await `(` `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : `set` PropertyName[?Yield, ?Await] `(` PropertySetParameterList `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition : `set` PropertyName `(` PropertySetParameterList `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : `set` PropertyName[?Yield, ?Await] `(` PropertySetParameterList `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Yield : `set` PropertyName_Yield `(` PropertySetParameterList `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : `set` PropertyName[?Yield, ?Await] `(` PropertySetParameterList `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Await : `set` PropertyName_Await `(` PropertySetParameterList `)` `{` FunctionBody `}`')

#MethodDefinition[Yield, Await]  : `set` PropertyName[?Yield, ?Await] `(` PropertySetParameterList `)` `{` FunctionBody[~Yield, ~Await] `}`
builder.r(w=1, d='MethodDefinition_Yield_Await : `set` PropertyName_Yield_Await `(` PropertySetParameterList `)` `{` FunctionBody `}`')

#PropertySetParameterList  : FormalParameter[~Yield, ~Await]
builder.r(w=1, d='PropertySetParameterList : FormalParameter')

#GeneratorMethod[Yield, Await]  : `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorMethod : `*` PropertyName `(` UniqueFormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorMethod[Yield, Await]  : `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorMethod_Yield : `*` PropertyName_Yield `(` UniqueFormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorMethod[Yield, Await]  : `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorMethod_Await : `*` PropertyName_Await `(` UniqueFormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorMethod[Yield, Await]  : `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorMethod_Yield_Await : `*` PropertyName_Yield_Await `(` UniqueFormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration : `function` `*` BindingIdentifier `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Yield : `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Await : `function` `*` BindingIdentifier_Await `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Yield_Await : `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Default : `function` `*` BindingIdentifier `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Yield_Default : `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Await_Default : `function` `*` BindingIdentifier_Await `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Yield_Await_Default : `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : [+Default] `function` `*` `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Default : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : [+Default] `function` `*` `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Yield_Default : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : [+Default] `function` `*` `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Await_Default : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorDeclaration[Yield, Await, Default]  : [+Default] `function` `*` `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorDeclaration_Yield_Await_Default : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorExpression  : `function` `*` BindingIdentifier[+Yield, ~Await]? `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorExpression : `function` `*` `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorExpression  : `function` `*` BindingIdentifier[+Yield, ~Await]? `(` FormalParameters[+Yield, ~Await] `)` `{` GeneratorBody `}`
builder.r(w=1, d='GeneratorExpression : `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield `)` `{` GeneratorBody `}`')

#GeneratorBody  : FunctionBody[+Yield, ~Await]
builder.r(w=1, d='GeneratorBody : FunctionBody_Yield')

#YieldExpression[In, Await]  : `yield`
builder.r(w=1, d='YieldExpression : `yield`')

#YieldExpression[In, Await]  : `yield`
builder.r(w=1, d='YieldExpression_In : `yield`')

#YieldExpression[In, Await]  : `yield`
builder.r(w=1, d='YieldExpression_Await : `yield`')

#YieldExpression[In, Await]  : `yield`
builder.r(w=1, d='YieldExpression_In_Await : `yield`')

#YieldExpression[In, Await]  : `yield`  AssignmentExpression[?In, +Yield, ?Await]
builder.r(w=1, d='YieldExpression : `yield` AssignmentExpression_Yield')

#YieldExpression[In, Await]  : `yield`  AssignmentExpression[?In, +Yield, ?Await]
builder.r(w=1, d='YieldExpression_In : `yield` AssignmentExpression_In_Yield')

#YieldExpression[In, Await]  : `yield`  AssignmentExpression[?In, +Yield, ?Await]
builder.r(w=1, d='YieldExpression_Await : `yield` AssignmentExpression_Yield_Await')

#YieldExpression[In, Await]  : `yield`  AssignmentExpression[?In, +Yield, ?Await]
builder.r(w=1, d='YieldExpression_In_Await : `yield` AssignmentExpression_In_Yield_Await')

#YieldExpression[In, Await]  : `yield`  `*` AssignmentExpression[?In, +Yield, ?Await]
builder.r(w=1, d='YieldExpression : `yield` `*` AssignmentExpression_Yield')

#YieldExpression[In, Await]  : `yield`  `*` AssignmentExpression[?In, +Yield, ?Await]
builder.r(w=1, d='YieldExpression_In : `yield` `*` AssignmentExpression_In_Yield')

#YieldExpression[In, Await]  : `yield`  `*` AssignmentExpression[?In, +Yield, ?Await]
builder.r(w=1, d='YieldExpression_Await : `yield` `*` AssignmentExpression_Yield_Await')

#YieldExpression[In, Await]  : `yield`  `*` AssignmentExpression[?In, +Yield, ?Await]
builder.r(w=1, d='YieldExpression_In_Await : `yield` `*` AssignmentExpression_In_Yield_Await')

#AsyncGeneratorMethod[Yield, Await]  : `async`  `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorMethod : `async` `*` PropertyName `(` UniqueFormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorMethod[Yield, Await]  : `async`  `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorMethod_Yield : `async` `*` PropertyName_Yield `(` UniqueFormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorMethod[Yield, Await]  : `async`  `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorMethod_Await : `async` `*` PropertyName_Await `(` UniqueFormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorMethod[Yield, Await]  : `async`  `*` PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorMethod_Yield_Await : `async` `*` PropertyName_Yield_Await `(` UniqueFormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration : `async` `function` `*` BindingIdentifier `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Yield : `async` `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Await : `async` `function` `*` BindingIdentifier_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Yield_Await : `async` `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Default : `async` `function` `*` BindingIdentifier `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Yield_Default : `async` `function` `*` BindingIdentifier_Yield `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Await_Default : `async` `function` `*` BindingIdentifier_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : `async`  `function` `*` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Yield_Await_Default : `async` `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `*` `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Default : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `*` `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Yield_Default : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `*` `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Await_Default : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `*` `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorDeclaration_Yield_Await_Default : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorExpression  : `async`  `function` `*` BindingIdentifier[+Yield, +Await]? `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorExpression : `async` `function` `*` `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorExpression  : `async`  `function` `*` BindingIdentifier[+Yield, +Await]? `(` FormalParameters[+Yield, +Await] `)` `{` AsyncGeneratorBody `}`
builder.r(w=1, d='AsyncGeneratorExpression : `async` `function` `*` BindingIdentifier_Yield_Await `(` FormalParameters_Yield_Await `)` `{` AsyncGeneratorBody `}`')

#AsyncGeneratorBody  : FunctionBody[+Yield, +Await]
builder.r(w=1, d='AsyncGeneratorBody : FunctionBody_Yield_Await')

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration : `class` BindingIdentifier ClassTail')

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Yield : `class` BindingIdentifier_Yield ClassTail_Yield')

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Await : `class` BindingIdentifier_Await ClassTail_Await')

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Yield_Await : `class` BindingIdentifier_Yield_Await ClassTail_Yield_Await')

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Default : `class` BindingIdentifier ClassTail')

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Yield_Default : `class` BindingIdentifier_Yield ClassTail_Yield')

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Await_Default : `class` BindingIdentifier_Await ClassTail_Await')

#ClassDeclaration[Yield, Await, Default]  : `class` BindingIdentifier[?Yield, ?Await] ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Yield_Await_Default : `class` BindingIdentifier_Yield_Await ClassTail_Yield_Await')

#ClassDeclaration[Yield, Await, Default]  : [+Default] `class` ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Default : `class` ClassTail')

#ClassDeclaration[Yield, Await, Default]  : [+Default] `class` ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Yield_Default : `class` ClassTail_Yield')

#ClassDeclaration[Yield, Await, Default]  : [+Default] `class` ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Await_Default : `class` ClassTail_Await')

#ClassDeclaration[Yield, Await, Default]  : [+Default] `class` ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassDeclaration_Yield_Await_Default : `class` ClassTail_Yield_Await')

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassExpression : `class` ClassTail')

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassExpression : `class` BindingIdentifier ClassTail')

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassExpression_Yield : `class` ClassTail_Yield')

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassExpression_Yield : `class` BindingIdentifier_Yield ClassTail_Yield')

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassExpression_Await : `class` ClassTail_Await')

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassExpression_Await : `class` BindingIdentifier_Await ClassTail_Await')

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassExpression_Yield_Await : `class` ClassTail_Yield_Await')

#ClassExpression[Yield, Await]  : `class` BindingIdentifier[?Yield, ?Await]? ClassTail[?Yield, ?Await]
builder.r(w=1, d='ClassExpression_Yield_Await : `class` BindingIdentifier_Yield_Await ClassTail_Yield_Await')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail : `{` `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail : `{` ClassBody `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail : ClassHeritage `{` `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail : ClassHeritage `{` ClassBody `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Yield : `{` `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Yield : `{` ClassBody_Yield `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Yield : ClassHeritage_Yield `{` `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Yield : ClassHeritage_Yield `{` ClassBody_Yield `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Await : `{` `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Await : `{` ClassBody_Await `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Await : ClassHeritage_Await `{` `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Await : ClassHeritage_Await `{` ClassBody_Await `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Yield_Await : `{` `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Yield_Await : `{` ClassBody_Yield_Await `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Yield_Await : ClassHeritage_Yield_Await `{` `}`')

#ClassTail[Yield, Await]  : ClassHeritage[?Yield, ?Await]? `{` ClassBody[?Yield, ?Await]? `}`
builder.r(w=1, d='ClassTail_Yield_Await : ClassHeritage_Yield_Await `{` ClassBody_Yield_Await `}`')

#ClassHeritage[Yield, Await]  : `extends` LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='ClassHeritage : `extends` LeftHandSideExpression')

#ClassHeritage[Yield, Await]  : `extends` LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='ClassHeritage_Yield : `extends` LeftHandSideExpression_Yield')

#ClassHeritage[Yield, Await]  : `extends` LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='ClassHeritage_Await : `extends` LeftHandSideExpression_Await')

#ClassHeritage[Yield, Await]  : `extends` LeftHandSideExpression[?Yield, ?Await]
builder.r(w=1, d='ClassHeritage_Yield_Await : `extends` LeftHandSideExpression_Yield_Await')

#ClassBody[Yield, Await]  : ClassElementList[?Yield, ?Await]
builder.r(w=1, d='ClassBody : ClassElementList')

#ClassBody[Yield, Await]  : ClassElementList[?Yield, ?Await]
builder.r(w=1, d='ClassBody_Yield : ClassElementList_Yield')

#ClassBody[Yield, Await]  : ClassElementList[?Yield, ?Await]
builder.r(w=1, d='ClassBody_Await : ClassElementList_Await')

#ClassBody[Yield, Await]  : ClassElementList[?Yield, ?Await]
builder.r(w=1, d='ClassBody_Yield_Await : ClassElementList_Yield_Await')

#ClassElementList[Yield, Await]  : ClassElement[?Yield, ?Await]
builder.r(w=1, d='ClassElementList : ClassElement')

#ClassElementList[Yield, Await]  : ClassElement[?Yield, ?Await]
builder.r(w=1, d='ClassElementList_Yield : ClassElement_Yield')

#ClassElementList[Yield, Await]  : ClassElement[?Yield, ?Await]
builder.r(w=1, d='ClassElementList_Await : ClassElement_Await')

#ClassElementList[Yield, Await]  : ClassElement[?Yield, ?Await]
builder.r(w=1, d='ClassElementList_Yield_Await : ClassElement_Yield_Await')

#ClassElementList[Yield, Await]  : ClassElementList[?Yield, ?Await] ClassElement[?Yield, ?Await]
builder.r(w=1, d='ClassElementList : ClassElementList ClassElement')

#ClassElementList[Yield, Await]  : ClassElementList[?Yield, ?Await] ClassElement[?Yield, ?Await]
builder.r(w=1, d='ClassElementList_Yield : ClassElementList_Yield ClassElement_Yield')

#ClassElementList[Yield, Await]  : ClassElementList[?Yield, ?Await] ClassElement[?Yield, ?Await]
builder.r(w=1, d='ClassElementList_Await : ClassElementList_Await ClassElement_Await')

#ClassElementList[Yield, Await]  : ClassElementList[?Yield, ?Await] ClassElement[?Yield, ?Await]
builder.r(w=1, d='ClassElementList_Yield_Await : ClassElementList_Yield_Await ClassElement_Yield_Await')

#ClassElement[Yield, Await]  : MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='ClassElement : MethodDefinition')

#ClassElement[Yield, Await]  : MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='ClassElement_Yield : MethodDefinition_Yield')

#ClassElement[Yield, Await]  : MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='ClassElement_Await : MethodDefinition_Await')

#ClassElement[Yield, Await]  : MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='ClassElement_Yield_Await : MethodDefinition_Yield_Await')

#ClassElement[Yield, Await]  : `static` MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='ClassElement : `static` MethodDefinition')

#ClassElement[Yield, Await]  : `static` MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='ClassElement_Yield : `static` MethodDefinition_Yield')

#ClassElement[Yield, Await]  : `static` MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='ClassElement_Await : `static` MethodDefinition_Await')

#ClassElement[Yield, Await]  : `static` MethodDefinition[?Yield, ?Await]
builder.r(w=1, d='ClassElement_Yield_Await : `static` MethodDefinition_Yield_Await')

#ClassElement[Yield, Await]  : `;`
builder.r(w=1, d='ClassElement : `;`')

#ClassElement[Yield, Await]  : `;`
builder.r(w=1, d='ClassElement_Yield : `;`')

#ClassElement[Yield, Await]  : `;`
builder.r(w=1, d='ClassElement_Await : `;`')

#ClassElement[Yield, Await]  : `;`
builder.r(w=1, d='ClassElement_Yield_Await : `;`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration : `async` `function` BindingIdentifier `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Yield : `async` `function` BindingIdentifier_Yield `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Await : `async` `function` BindingIdentifier_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Yield_Await : `async` `function` BindingIdentifier_Yield_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Default : `async` `function` BindingIdentifier `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Yield_Default : `async` `function` BindingIdentifier_Yield `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Await_Default : `async` `function` BindingIdentifier_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : `async`  `function` BindingIdentifier[?Yield, ?Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Yield_Await_Default : `async` `function` BindingIdentifier_Yield_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Default : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Yield_Default : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Await_Default : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionDeclaration[Yield, Await, Default]  : [+Default] `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionDeclaration_Yield_Await_Default : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionExpression  : `async`  `function` `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionExpression : `async` `function` `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionExpression  : `async`  `function` BindingIdentifier[~Yield, +Await] `(` FormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncFunctionExpression : `async` `function` BindingIdentifier_Await `(` FormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncMethod[Yield, Await]  : `async`  PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncMethod : `async` PropertyName `(` UniqueFormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncMethod[Yield, Await]  : `async`  PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncMethod_Yield : `async` PropertyName_Yield `(` UniqueFormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncMethod[Yield, Await]  : `async`  PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncMethod_Await : `async` PropertyName_Await `(` UniqueFormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncMethod[Yield, Await]  : `async`  PropertyName[?Yield, ?Await] `(` UniqueFormalParameters[~Yield, +Await] `)` `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncMethod_Yield_Await : `async` PropertyName_Yield_Await `(` UniqueFormalParameters_Await `)` `{` AsyncFunctionBody `}`')

#AsyncFunctionBody  : FunctionBody[~Yield, +Await]
builder.r(w=1, d='AsyncFunctionBody : FunctionBody_Await')

#AwaitExpression[Yield]  : `await` UnaryExpression[?Yield, +Await]
builder.r(w=1, d='AwaitExpression : `await` UnaryExpression_Await')

#AwaitExpression[Yield]  : `await` UnaryExpression[?Yield, +Await]
builder.r(w=1, d='AwaitExpression_Yield : `await` UnaryExpression_Yield_Await')

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
builder.r(w=1, d='AsyncArrowFunction : `async` AsyncArrowBindingIdentifier `=>` AsyncConciseBody')

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
builder.r(w=1, d='AsyncArrowFunction_In : `async` AsyncArrowBindingIdentifier `=>` AsyncConciseBody_In')

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
builder.r(w=1, d='AsyncArrowFunction_Yield : `async` AsyncArrowBindingIdentifier_Yield `=>` AsyncConciseBody')

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
builder.r(w=1, d='AsyncArrowFunction_In_Yield : `async` AsyncArrowBindingIdentifier_Yield `=>` AsyncConciseBody_In')

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
builder.r(w=1, d='AsyncArrowFunction_Await : `async` AsyncArrowBindingIdentifier `=>` AsyncConciseBody')

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
builder.r(w=1, d='AsyncArrowFunction_In_Await : `async` AsyncArrowBindingIdentifier `=>` AsyncConciseBody_In')

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
builder.r(w=1, d='AsyncArrowFunction_Yield_Await : `async` AsyncArrowBindingIdentifier_Yield `=>` AsyncConciseBody')

#AsyncArrowFunction[In, Yield, Await]  : `async`  AsyncArrowBindingIdentifier[?Yield]  `=>` AsyncConciseBody[?In]
builder.r(w=1, d='AsyncArrowFunction_In_Yield_Await : `async` AsyncArrowBindingIdentifier_Yield `=>` AsyncConciseBody_In')

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
builder.r(w=1, d='AsyncArrowFunction : CoverCallExpressionAndAsyncArrowHead `=>` AsyncConciseBody')

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
builder.r(w=1, d='AsyncArrowFunction_In : CoverCallExpressionAndAsyncArrowHead `=>` AsyncConciseBody_In')

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
builder.r(w=1, d='AsyncArrowFunction_Yield : CoverCallExpressionAndAsyncArrowHead_Yield `=>` AsyncConciseBody')

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
builder.r(w=1, d='AsyncArrowFunction_In_Yield : CoverCallExpressionAndAsyncArrowHead_Yield `=>` AsyncConciseBody_In')

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
builder.r(w=1, d='AsyncArrowFunction_Await : CoverCallExpressionAndAsyncArrowHead_Await `=>` AsyncConciseBody')

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
builder.r(w=1, d='AsyncArrowFunction_In_Await : CoverCallExpressionAndAsyncArrowHead_Await `=>` AsyncConciseBody_In')

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
builder.r(w=1, d='AsyncArrowFunction_Yield_Await : CoverCallExpressionAndAsyncArrowHead_Yield_Await `=>` AsyncConciseBody')

#AsyncArrowFunction[In, Yield, Await]  : CoverCallExpressionAndAsyncArrowHead[?Yield, ?Await]  `=>` AsyncConciseBody[?In] #callcover
builder.r(w=1, d='AsyncArrowFunction_In_Yield_Await : CoverCallExpressionAndAsyncArrowHead_Yield_Await `=>` AsyncConciseBody_In')

#AsyncConciseBody[In]  :   AssignmentExpression[?In, ~Yield, +Await]
builder.r(w=1, d='AsyncConciseBody : AssignmentExpression_Await')

#AsyncConciseBody[In]  :   AssignmentExpression[?In, ~Yield, +Await]
builder.r(w=1, d='AsyncConciseBody_In : AssignmentExpression_In_Await')

#AsyncConciseBody[In]  : `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncConciseBody : `{` AsyncFunctionBody `}`')

#AsyncConciseBody[In]  : `{` AsyncFunctionBody `}`
builder.r(w=1, d='AsyncConciseBody_In : `{` AsyncFunctionBody `}`')

#AsyncArrowBindingIdentifier[Yield]  : BindingIdentifier[?Yield, +Await]
builder.r(w=1, d='AsyncArrowBindingIdentifier : BindingIdentifier_Await')

#AsyncArrowBindingIdentifier[Yield]  : BindingIdentifier[?Yield, +Await]
builder.r(w=1, d='AsyncArrowBindingIdentifier_Yield : BindingIdentifier_Yield_Await')

#CoverCallExpressionAndAsyncArrowHead[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CoverCallExpressionAndAsyncArrowHead : MemberExpression Arguments')

#CoverCallExpressionAndAsyncArrowHead[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CoverCallExpressionAndAsyncArrowHead_Yield : MemberExpression_Yield Arguments_Yield')

#CoverCallExpressionAndAsyncArrowHead[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CoverCallExpressionAndAsyncArrowHead_Await : MemberExpression_Await Arguments_Await')

#CoverCallExpressionAndAsyncArrowHead[Yield, Await]  : MemberExpression[?Yield, ?Await] Arguments[?Yield, ?Await]
builder.r(w=1, d='CoverCallExpressionAndAsyncArrowHead_Yield_Await : MemberExpression_Yield_Await Arguments_Yield_Await')

#AsyncArrowHead  : `async`  ArrowFormalParameters[~Yield, +Await]
builder.r(w=1, d='AsyncArrowHead : `async` ArrowFormalParameters_Await')

