import ply.yacc as yacc
from cclex import tokens
import action


def p_command_seq(p):
    '''
    command_seq : command_block
                | command_seq command_block
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1].update(p[2])
        p[0] = p[1]

def p_command_block(p):
    'command_block : COMMAND PHRASE action_seq END'
    p[0] = {p[2] : p[3]}

def p_action_seq(p):
    '''
    action_seq : action
               | action_seq action
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_action(p):
    '''
    action : key_decl
           | DELAY NUMBER
           | MULTI key_seq END
    '''
    if len(p) == 2:
        p[0] = action.KeyAction(p[1])
    elif len(p) == 3:
        p[0] = action.DelayAction(p[2] / 1000)
    else:
        p[0] = action.HotkeyAction(p[2])

def p_key_seq(p):
    '''
    key_seq : key_decl
            | key_seq key_decl
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_key_decl(p):
    'key_decl : KEY KEYVAL'
    p[0] = p[2]


def p_error(p):
    print("Syntax error at ({}, {}): '{}'".format(p.lineno,
                                                p.lexpos,
                                                p.value))


parser = yacc.yacc()
