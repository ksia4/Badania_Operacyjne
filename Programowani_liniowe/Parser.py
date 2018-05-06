# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

def znajdz_maksymalny_indeks_x(data):
    max_ind = -1
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        if tok.type == 'X' and tok.value > max_ind:
            max_ind = tok.value
    return max_ind


# List of token names.   This is always required
tokens = (
   'NUMBER',
   'DOT',
   'PLUS',
   'ZMIENNA',
   'X',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'GRE_OR_EQ',
   'LE_OR_EQ',
   'EQUAL',
   'GREATER',
   'LESS',
   'LPAREN',
   'RPAREN',

)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
# t_DOT     = r'\.'
t_GRE_OR_EQ = r'>='
t_LE_OR_EQ= r'<='
t_EQUAL   = r'\='
t_GREATER = r'\>'
t_LESS    = r'\<'


def t_X(t):
    r'x\d+'
    t.value = int(t.value[1:])
    return t

def t_ZMIENNA(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# # Test it out
# data = '''
# 3 + 4 * 10.5
#   + -20 *x2
# '''
#
# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
#
# print("Ten drugi tekst")

# Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
#
# print("Podaj równanie")
# data = input(' ')
# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     if tok.type == 'X':
#         print(tok.value)
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
