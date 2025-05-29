def is_funny(string): return False not in list(map(lambda char: char == "h" or char == "a" , string ))

print(is_funny("haaaaaaaaahhhh"))
