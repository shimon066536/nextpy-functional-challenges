import itertools

wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

for i in range(len(wallet)):
    iter = (itertools.combinations(wallet, i))
    for i in iter:
        if sum(i) == 100:
            print(i)
