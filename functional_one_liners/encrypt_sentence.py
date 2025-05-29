# password = 'sljmai ugrf rfc ambc: lglc dmsp mlc rum'

password = input("Enter sentence: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(letter): return chr(ord(letter) + 2)
print(''.join(list(map(encrypt, password))).replace('"', ' '))
