class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

class Uppercase(PasswordMissingCharacter):
    def __str__(self):
        return f"The password {self._arg} is missing a character (Uppercase)."

class Lowercase(PasswordMissingCharacter):
    def __str__(self):
        return f"The password {self._arg} is missing a character (Lowercase)."

class Digit(PasswordMissingCharacter):
    def __str__(self):
        return f"The password {self._arg} is missing a character (Digit)."

class Special(PasswordMissingCharacter):
    def __str__(self):
        return f"The password {self._arg} is missing a character (Special)."

class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"The password {self._arg} is too short."

class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"The password {self._arg} is too long."
