class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        x = re.search("\W", self._arg)
        return 'The username %s contains an illegal character "%s" at index %s.' %(self._arg, x.group(), x.span()[1])
    def get_arg(self):
        return self._arg

class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The username %s is too short." %self._arg
    def get_arg(self):
        return self._arg

class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The username %s is too long." %self._arg
    def get_arg(self):
        return self._arg

class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The password %s is missing a character." %self._arg
    def get_arg(self):
        return self._arg
class Uppercase(PasswordMissingCharacter):
    def __str__(self):
        super().__str__()
        return "The password %s is missing a character (Uppercase)." %self._arg
class Lowercase(PasswordMissingCharacter):
    def __str__(self):
        super().__str__()
        return "The password %s is missing a character (Lowercase)." %self._arg
class Digit(PasswordMissingCharacter):
    def __str__(self):
        super().__str__()
        return "The password %s is missing a character (Digit)." %self._arg
class Special(PasswordMissingCharacter):
    def __str__(self):
        super().__str__()
        return "The password %s is missing a character (Special)." %self._arg

class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The password %s is too short." %self._arg
    def get_arg(self):
        return self._arg

class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The password %s is too long." %self._arg
    def get_arg(self):
        return self._arg

import re, string

def check_input(username, password):
    try:
        check_UsernameContainsIllegalCharacter = re.search("\W", username)
        check_UsernameTooShort = len(username) < 3
        check_UsernameTooLong = len(username) > 16
        check_PasswordTooShort = len(password) < 8
        check_PasswordTooLong = len(password) > 40
        check_PasswordMissingCharacter_Uppercase = not (re.search("[A-Z]", password))
        check_PasswordMissingCharacter_Lowercase = not (re.search("[a-z]", password))
        check_PasswordMissingCharacter_Digit = not (re.search("[0-9]", password))
        check_PasswordMissingCharacter_Special = not ([i for i in password if i in string.punctuation])

        if check_UsernameContainsIllegalCharacter:
            raise UsernameContainsIllegalCharacter(username)
        elif check_UsernameTooShort:
            raise UsernameTooShort(username)
        elif check_UsernameTooLong:
            raise UsernameTooLong(username)
        elif check_PasswordTooShort:
            raise PasswordTooShort(password)
        elif check_PasswordTooLong:
            raise PasswordTooLong(password)
        elif check_PasswordMissingCharacter_Uppercase:
            raise Uppercase(password)
        elif check_PasswordMissingCharacter_Lowercase:
            raise Lowercase(password)
        elif check_PasswordMissingCharacter_Digit:
            raise Digit(password)
        elif check_PasswordMissingCharacter_Special:
            raise Special(password)
        else: print('Ok')

    except UsernameContainsIllegalCharacter:
        print(UsernameContainsIllegalCharacter(username))
    except UsernameTooShort:
        print(UsernameTooShort(username))
    except UsernameTooLong:
        print(UsernameTooLong(username))
    except PasswordTooShort:
        print(PasswordTooShort(password))
    except PasswordTooLong:
        print(PasswordTooLong(password))
    except Uppercase:
        print(Uppercase(password))
    except Lowercase:
        print(Lowercase(password))
    except Digit:
        print(Digit(password))
    except Special:
        print(Special(password))

def main():
    check_input("1", "2") # The username is too short
    check_input("0123456789ABCDEFG", "2") # The username is too long
    check_input("A_a1.", "12345678") # The username contains an illegal character
    check_input("A_1", "2") # The password is too short
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary") # The password is too long
    check_input("A_1", "abcdefghijklmnop") # The password is missing a character
    check_input("A_1", "ABCDEFGHIJLKMNOP") # The password is missing a character
    check_input("A_1", "ABCDEFGhijklmnop") # The password is missing a character
    check_input("A_1", "4BCD3F6h1jk1mn0p") # The password is missing a character
    check_input("A_1", "4BCD3F6.1jk1mn0p") # Ok

if __name__ == '__main__':
    main()
