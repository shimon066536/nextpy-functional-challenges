"""
fibonacci_generator.py

This script demonstrates a generator that yields Fibonacci numbers under 100.
"""

def get_fibo():
    number1 = 0
    number2 = 1
    while number1 < 100:
        yield number1
        yield number2
        number1 += number2
        number2 += number1

def main():
    fibo_gen = get_fibo()
    for _ in range(6):
        print(next(fibo_gen))

if __name__ == "__main__":
    main()
