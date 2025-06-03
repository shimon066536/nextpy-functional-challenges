def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def first_prime_over(n): return (i for i in range(n, 10**10) if is_prime(i) == True)

print(next(first_prime_over(10000000)))
