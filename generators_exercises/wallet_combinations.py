
"""
wallet_combinations.py

Finds all combinations of coins and bills in a wallet that sum to exactly 100.
"""

import itertools

def main():
    wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    for i in range(1, len(wallet) + 1):
        combos = itertools.combinations(wallet, i)
        for c in combos:
            if sum(c) == 100:
                print(c)

if __name__ == "__main__":
    main()
