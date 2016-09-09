import ply.lex as lex


#  define list of tokens
tokens = [
        'COMMAND',
        'MULTI',
        'KEY',
        'END',
        'DELAY',
        'NUMBER',
        'KEYVAL',
        'PHRASE'
]


#  define variables for generating regex
escape_keys     = r'[\t\n\r\s]'
symbol_keys     = r'[\W_]'
f_keys          = r'f[1-9][0-9]?'
numpad_keys     = r'num[0-9]'
special_keys    = r'launchapp[12]'



#  define basic token regex
t_COMMAND   = r'COMMAND'
t_MULTI     = r'MULTI'
t_KEY       = r'KEY'
t_END       = r'END'
t_DELAY     = r'DELAY'
t_KEYVAL    = r'([a-z]+|[0-9]|{}|{}|{}|{}|{})'.format(escape_keys,
                                                      symbol_keys,
                                                      f_keys,
                                                      numpad_keys,
                                                      special_keys)


#  define token regex that require further computation
def t_NUMBER(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    return t

def t_PHRASE(t):
    r'"([a-zA-Z0-9]+\s?)+"'
    t.value = eval(t.value)
    return t


#  define ignored characters
t_ignore = ' \t'


#  define error function
def t_error(t):
    print('Illegal character "{}"'.format(t.value[0]))
    t.lexer.skip(1)


#  define utility
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#  generate lexer
lexer = lex.lex()
