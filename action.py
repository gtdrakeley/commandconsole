from collections import namedtuple
from pyautogui import press, hotkey
from time import sleep


Command = namedtuple("Command", ["func", "args", "nxt"])


class Action:
    def __init__(self, args):
        self.args = args

    def execute(self):
        raise NotImplementedError

    def tuplefy(self):
        raise NotImplementedError


class KeyAction(Action):
    def execute(self):
        press(self.args)

class HotkeyAction(Action):
    def execute(self):
        hotkey(*args)


class DelayAction(Action):
    def execute(self):
        sleep(self.args)
