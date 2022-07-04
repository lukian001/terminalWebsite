from enum import Enum


class Commands(Enum):
    HELP = 'help'
    CLEAR = 'clear'
    SOCIAL = 'social'
    WELCOME = 'welcome'
    CHANGE_WALLPAPER = 'changeBackground'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
