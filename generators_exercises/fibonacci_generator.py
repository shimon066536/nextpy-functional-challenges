def get_fibo():
    number1 = 0
    number2 = 1
    while number1 < 100:
        yield number1
        yield number2
        number1 += number2
        number2 += number1


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
