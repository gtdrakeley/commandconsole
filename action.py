from collections import namedtuple


Command = namedtuple("Command", ["func", "args", "nxt"])


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
