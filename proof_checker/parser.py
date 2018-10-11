import ply.yacc as yacc
import sys
from lexer import tokens



precedence = (
        ('left', 'IMPLIES'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('right', 'NOT'),
        ('right', 'SAYS'),
        ('left', 'EQUIVALENT'),
        ('nonassoc', 'CAN_ACCESS','CONTROLS'),
        ('left', 'SAYS'),
        ('left', 'SAYS_FOR'),

    )

rule = []

def p_start(p):
  'start : proof'
  rule.append(0)

def p_proof_without_givens(p):
	'proof : to_prove lines'
	rule.append(1)

def p_proof_with_givens(p):
	'proof : to_prove givens lines'
	rule.append(2)

def p_givens_multiple(p):
	'givens : givens given'
	rule.append(3)

def p_givens(p):
	'givens : given'
	rule.append(4)

def p_given(p):
	'given : LINENUM statement GIVEN'
	rule.append(5)

def p_to_prove(p):
	'to_prove : LINENUM statement TO_PROVE'
	rule.append(6)

def p_lines_multiple(p):
	'lines : lines line'
	rule.append(7)

def p_lines(p):
	'lines : line'
	rule.append(8)

def p_line_2refs(p):
	'line : LINENUM statement REASON LINENUM LINENUM SEMICOLON'
	rule.append(9)
	
def p_line_1ref(p):
	'line : LINENUM statement REASON LINENUM SEMICOLON'
	rule.append(10)

def p_line_noref(p):
	'line : LINENUM statement REASON SEMICOLON'
	rule.append(11)

def p_statement(p):
	'statement : OBJECT'
	rule.append(12)

def p_statement_and(p):
	'statement : statement AND statement'
	rule.append(13)

def p_statement_or(p):
	'statement : statement OR statement'
	rule.append(14)

def p_statement_implies(p):
	'statement : statement IMPLIES statement'
	rule.append(15)

def p_statement_equivalent(p):
	'statement : statement EQUIVALENT statement'
	rule.append(16)

def p_statement_not(p):
	'statement : NOT statement'
	rule.append(17)

def p_statement_says(p):
	'statement : PRINCIPLE SAYS statement'
	rule.append(18)

def p_statement_parens(p):
	'statement : LPAREN statement RPAREN'
	rule.append(19)

def p_statement_says_for(p):
	'statement : PRINCIPLE SAYS_FOR PRINCIPLE'
	rule.append(20)

def p_statement_controls(p):
	'statement : PRINCIPLE CONTROLS statement'
	rule.append(21)



def p_error(p):
  """Error rule for Syntax Errors handling and reporting."""
  print("-------------------------- Error ---------------------------------")
  if p is None:
    print("Error! Unexpected end of input!")
  else:
    error = "Syntax error! Line: {}, position: {}, character: {}, type: {}".format(p.lineno, p.lexpos, p.value, p.type)
    print rule
    print(error)
    print type(p.type)
  print("Exiting .....")
  exit()



parser  = yacc.yacc()




input_file = sys.argv[1]
with open(input_file) as file:
    data = file.read()
parser.parse(data)


# for s in SymbolTables:
#   print("===========")
#   s.printsymtab()
# print("===========")



# print(len(SymbolTables))
# for t in ClassTable:
#   print ClassTable[t].printClass()

print(".... Parsing .... done ....\n")

print rule
