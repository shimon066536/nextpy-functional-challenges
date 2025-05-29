import re

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        x = re.search(r"\W", self._arg)
        return f'The username {self._arg} contains an illegal character "{x.group()}" at index {x.span()[1]}.'

class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"The username {self._arg} is too short."

class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"The username {self._arg} is too long."
