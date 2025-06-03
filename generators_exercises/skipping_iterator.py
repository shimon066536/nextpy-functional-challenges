"""
skipping_iterator.py

Demonstrates iterating over a range while skipping multiple elements per iteration.
"""

def main():
    numbers = iter(range(1, 1030))
    while True:
        try:
            print(next(numbers))
            for _ in range(3):  # skip 3 elements
                next(numbers)
        except StopIteration:
            break

if __name__ == "__main__":
    main()
