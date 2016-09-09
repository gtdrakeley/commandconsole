import ply.yacc as yacc
from cclex import tokens
import action


#  define grammar rules
def p_command_sequence(p):
    '''
    CommSeq : CommBlock
            | CommSeq CommBlock
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1].update(p[2])
        p[0] = p[1]

def p_command_block(p):
    'CommBlock : COMMAND PHRASE ActionSeq END'
    p[0] = {p[2] : p[3]}

def p_action_sequence(p):
    '''
    ActionSeq : Action
              | ActionSeq Action
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_action(p):
    '''
    Action : KeyDecl
           | DELAY NUMBER
           | MULTI KeySeq END
    '''
    if len(p) == 2:
        p[0] = action.KeyAction(p[1])
    elif len(p) == 3:
        p[0] = action.DelayAction(p[2] / 1000)
    else:
        p[0] = action.HotkeyAction(p[2])

def p_key_sequence(p):
    '''
    KeySeq : KeyDecl
           | KeySeq KeyDecl
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_key_declaration(p):
    'KeyDecl : KEY KEYVAL'
    p[0] = p[2]


#  define error function
def p_error(p):
    print("Syntax error at ({}, {}): '{}'".format(p.lineno,
                                                p.lexpos,
                                                p.value))


parser = yacc.yacc()
