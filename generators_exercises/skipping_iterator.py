numbers = iter(list(range(1, 1030)))
for i in numbers:
    print(i)
    next(numbers)
    next(numbers)
    next(numbers)
