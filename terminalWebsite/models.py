from enum import Enum


class Social:
    def __init__(self, app, address):
        self.app = app
        self.address = address


class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Socials(Enum):
    LINKEDIN = Social('LinkedIn', 'linkedin.com/in/lucian-streulea-37194a237/')
    INSTA = Social('Instagram', 'instagram.com/lukian001')
    FACEBOOK = Social('Facebook', 'facebook.com/streulea.lucian.1/')
    TWITTER = Social('Twitter', 'redacted')
    REDDIT = Social('Reddit', 'redacted')

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Commands(Enum):
    HELP = Command('help', 'This command will print all available commands.')
    CLEAR = Command('clear', 'This command will clear the screen.')
    SOCIAL = Command('social', 'This command will print all available social media links used by me.')
    WELCOME = Command('welcome', 'This command will print the welcome message.')
    CHANGE_WALLPAPER = Command('changeBackground', 'This command will change the background.')

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
