from enum import Enum


class Commands(Enum):
    HELP = 'help'
    CLEAR = 'clear'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
