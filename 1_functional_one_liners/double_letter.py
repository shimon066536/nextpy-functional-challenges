def do_le(word):
    return word * 2

def double_letter(my_str):
    return ''.join(list(map(do_le, my_str)))

print(double_letter("python"))
print(double_letter("we are the champions!"))
