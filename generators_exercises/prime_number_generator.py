"""
prime_generator.py

Generates prime numbers starting from a given number using a generator expression.
"""

def is_prime(n):
    """Returns True if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    """Returns a generator yielding prime numbers starting from n."""
    return (i for i in range(n, 10**10) if is_prime(i))

def main():
    start = 10_000_000
    gen = first_prime_over(start)
    print(f"First prime number over {start} is: {next(gen)}")

if __name__ == "__main__":
    main()
