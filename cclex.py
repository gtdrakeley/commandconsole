import ply.lex as lex


tokens = [
        "COMMAND",
        "DELAY",
        "END",
        "NUMBER",
        "KEY",
        "PHRASE",
        "COMMA",
        "LPAREN",
        "RPAREN"
]

escape_keys     = r"[\t\n\r\s]"
symbol_keys     = r"[\W_]"
f_keys          = r"f[1-9][0-9]?"
numpad_keys     = r"num[0-9]"
special_keys    = r"launchapp[12]"
key             = r"\[([a-z]+|[0-9]|{}|{}|{}|{}|{})\]".format(escape_keys,
                                                              symbol_keys,
                                                              f_keys,
                                                              numpad_keys,
                                                              special_keys)

t_COMMAND   = r"COMMAND"
t_DELAY     = r"DELAY"
t_END       = r"END"
t_COMMA     = r","
t_LPAREN    = r"\("
t_RPAREN    = r"\)"

@lex.TOKEN(key)
def t_KEY(t):
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r"[1-9][0-9]*"
    t.value = int(t.value)
    return t

def t_PHRASE(t):
    r"\"([a-zA-Z0-9]+\s?)+\""
    t.value = eval(t.value)
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore = " \t"

def t_error(t):
    print("Illegal character \"{}\"".format(t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
