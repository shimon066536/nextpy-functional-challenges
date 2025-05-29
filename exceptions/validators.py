from .username_exceptions import UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong
from .password_exceptions import PasswordTooShort, PasswordTooLong, Uppercase, Lowercase, Digit, Special
import re, string

def check_input(username, password):
    try:
        if re.search(r"\W", username):
            raise UsernameContainsIllegalCharacter(username)
        elif len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
        elif not re.search(r"[A-Z]", password):
            raise Uppercase(password)
        elif not re.search(r"[a-z]", password):
            raise Lowercase(password)
        elif not re.search(r"\d", password):
            raise Digit(password)
        elif not any(c in string.punctuation for c in password):
            raise Special(password)
        else:
            print("Ok")

    except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
            PasswordTooShort, PasswordTooLong, Uppercase, Lowercase, Digit, Special) as e:
        print(e)

def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

if __name__ == '__main__':
    main()
