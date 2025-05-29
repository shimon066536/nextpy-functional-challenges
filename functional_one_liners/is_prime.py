# def is_prime(number): return [i for i in range(2, ((number//2)+1)) if number % i == 0]
# def is_prime(number): return True in (number % i == 0 for i in range(2, number))


def is_prime(number): return len(list(filter(lambda num: number % num == 0, range(2, number)))) == 0

print(is_prime(43))
print(is_prime(42))
