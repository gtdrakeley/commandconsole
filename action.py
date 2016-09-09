from collections import namedtuple
from pyautogui import press, hotkey
from time import sleep


Command = namedtuple("Command", ["func", "args", "nxt"])


"""
class Action:
    def __init__(self, func, args):
        self.func = func
        self.args = args
        self.nxt = None

    def chain(self, nxt):
        if self.nxt is None:
            self.nxt = nxt
        else:
            self.nxt.chain(nxt)

    def tuplefy(self):
        if self.nxt is None:
            return Command(self.func, self.args, None)
        else:
            return Command(self.func, self.args, self.nxt.tuplefy())
"""

class Action:
    def __init__(self, args):
        self.args = args
        self.nxt = None

    def execute(self):
        raise NotImplementedError

    def tuplefy(self):
        raise NotImplementedError


class KeyAction(Action):
    def execute(self):
        press(self.args)
        if self.nxt is not None:
            self.nxt.execute()

class HotkeyAction(Action):
    def execute(self):
        hotkey(*args)
        if self.nxt is not None:
            self.nxt.execute()


class DelayAction(Action):
    def execute(self):
        sleep(self.args)
        if self.nxt is not None:
            self.nxt.execute()
