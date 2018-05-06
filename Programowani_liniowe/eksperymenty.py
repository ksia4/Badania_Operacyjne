import funkcja
import zbior_funkcji
import random
import matplotlib.pyplot as plt
import Parser
import ply.lex as lex

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

def znajdz_wspolczynniki(data):
    lexer.input(data)
    wsp = []
    mam_go = False
    temp = float(1)
    minus = False
    wyraz_wolny = float(0)
    times_po_liczbie = False
    while True:
        tok = lexer.token()
        if not tok:
            break

        if tok.type == 'MINUS':
            minus = True

        if (tok.type =='NUMBER' or tok.type == 'DIVIDE' or tok.type == 'ZMIENNA') and mam_go:
            znak = 1
            if minus:
                znak = -1
            wyraz_wolny = znak * tok.value
            mam_go = False

        if tok.type =='NUMBER' or tok.type == 'DIVIDE' or tok.type == 'ZMIENNA':
            temp = tok.value
            mam_go = True
        if tok.type == 'TIMES' and mam_go:
            times_po_liczbie = True
            mam_go = False
        if tok.type == 'X':
            ind = int(tok.value)
            while len(wsp) < (ind-1):
                wsp.append(float(0))
            if minus:
                temp = -1*temp
                minus = False
            wsp.append(temp)
            temp = float(1)
            mam_go = False
            times_po_liczbie = False

    print(wsp)
    if wyraz_wolny != 0:
        print("Wyraz wolny = " + str(wyraz_wolny))
    return [wsp, wyraz_wolny]

def rozpoznaj_znak(warunek):
    lexer.input(warunek)
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'GRE_OR_EQ' or tok.type == 'LE_OR_EQ' or tok.type == 'EQUAL'\
                or tok.type == 'GREATER' or tok.type == 'LESS':
            return tok.value
    return -1



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
# t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
# t_DOT     = r'\.'
t_GRE_OR_EQ = r'\>\='
t_LE_OR_EQ= r'\<\='
t_EQUAL   = r'\='
t_GREATER = r'\>'
t_LESS    = r'\<'


def t_DIVIDE(t):
    r'\d+\/\d+'
    temp = t.value.split('/')
    t.value = float(float(temp[0])/float(temp[1]))
    return t

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

def istnieje_niezerowy_wyraz_wolny_f_celu(dane):
    istnieje = False
    Parser.lexer.input(dane)

# def zrob_dzielenie(dane):
#     temp = dane.replace(" ", "")
#     tablica = temp.split('\\')
#     data2 = ""
#     for i in range(len(tablica) - 1):
#         wart = tablica[i][]


# Build the lexer
lexer = lex.lex()


if __name__ == '__main__':

    # # Test it out
    data = '''
    3 + 4 * 10.5
      + -20/5 *x2
    '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok.value)

    data = input('f(X) = ')
    znajdz_wspolczynniki(data)
    warunek = input('Podaj jakis warunek ')
    znak = rozpoznaj_znak(warunek)
    print(znak)
    print("To był znak")
    [rownanie, wyraz_wolny] = warunek.split(znak)
    print(wyraz_wolny)
    print("A współczynniki:")
    znajdz_wspolczynniki(rownanie)

    # print("Witaj w programie który rozwiąże Twój problem")
    # tryb = -1
    # max_or_min = ''
    # while tryb < 0:
    #     print("Czy będziemy maksymalizować czy minimalizować funkcję celu? [max/min]")
    #     max_or_min = input(' ')
    #     # 0 - minimalizacja
    #     # 1 - maksymalizacja
    #     if max_or_min == 'max':
    #         tryb = 1
    #     elif max_or_min == 'min':
    #         tryb = 0
    #     else:
    #         print("Proszę wpisać max lub min :)")
    # print(tryb)
    # funkcja_celu = funkcja.Funkcja(max_or_min)
    #
    # dane = input('Podaj funkcje celu F(X) = ')
    #
    # dane2 = zrob_dzielenie(dane)
    # if istnieje_niezerowy_wyraz_wolny_f_celu(dane):
    #     print("TAK!")
    # Parser.lexer.input(dane)
    #
