import ply.yacc as yacc
from cclex import tokens
from cclex import test_data1, test_data2, test_data3
from cclex import test_data4, test_data5, test_data6
from cclex import test_data7, test_data8
from action import Action
from pyautogui import press, hotkey
from time import sleep


def p_command_sequence(p):
    """
    command_sequence : command_block
                     | command_sequence command_block
    """
    if len(p) == 2:
        p[0] = {p[1][0] : p[1][1]}
    else:
        p[1][p[2][0]] = p[2][1]
        p[0] = p[1]

def p_command_block(p):
    "command_block : COMMAND PHRASE action_sequence END"
    p[0] = (p[2], p[3].tuplefy())

def p_action_sequence(p):
    """
    action_sequence : action
                    | action_sequence COMMA action
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1].chain(p[3])
        p[0] = p[1]

def p_action(p):
    """
    action : KEY
           | DELAY NUMBER
           | LPAREN key_sequence RPAREN
    """
    if len(p) == 2:
        p[0] = Action(press, p[1])
    elif len(p) == 3:
        p[0] = Action(sleep, p[2] / 1000)
    else:
        p[0] = Action(hotkey, p[2])

def p_key_sequence(p):
    """
    key_sequence : KEY
                 | key_sequence COMMA KEY
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].extend([p[3]])
        p[0] = p[1]


def p_error(p):
    print("Syntax error at ({}, {}): '{}'".format(p.lineno,
                                                p.lexpos,
                                                p.value))


parser = yacc.yacc()
