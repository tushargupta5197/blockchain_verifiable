import ply.lex as lex

tokens = (
	'LINENUM',
	'PRINCIPLE',
	'AND',
	'OR',
	'IMPLIES',
	'NOT',
	'EQUIVALENT',
	'DERIVES',
	'SAYS',
	'SAYS_FOR',
	'CONTROLS',
	'CAN_ACCESS',
	'OBJECT',
	'LPAREN',
	'RPAREN',
	'REASON',
	'TO_PROVE',
	'GIVEN',
	'SEMICOLON',
	'TRUE',
	'FALSE',
	#'COMMA',
)

reserved = {
	'can_access' : 'CAN_ACCESS',
	'says' : 'SAYS',
	'says_for' : 'SAYS_FOR',
	'controls' : 'CONTROLS',
	'@To_Prove' : 'TO_PROVE',
	'@Given' : 'GIVEN',
	'true' : 'TRUE',
	'false' : 'FALSE',

}


t_AND = r'&'
t_OR = r'\|'
t_IMPLIES = r'->'
t_EQUIVALENT = r'<->'
t_DERIVES = r'\|-'



# t_SAYS = r'says'
# t_CAN_ACCESS = r'can_access'
# t_SAYS_FOR = r'says_for'
# t_CONTROLS = r'controls'

t_LINENUM = r'[0-9]+'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMICOLON = r';'
# t_COMMA = r','

def t_PRINCIPLE(t):
	r'[A-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'PRINCIPLE')
	return t

def t_OBJECT(t):
	r'[a-z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'OBJECT')
	return t

def t_REASON(t):
	r'@[A-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'REASON')
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t,'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()



data = '''
(P says (Q says s1)) -> s1, P says_for Q |- Q controls P
'''
lexer.input(open('sample_solution.csv').read())
while True:
	tok = lexer.token()
	if not tok:
		break
	print tok
