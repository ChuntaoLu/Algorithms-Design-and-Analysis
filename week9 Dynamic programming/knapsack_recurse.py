import sys
import time
sys.setrecursionlimit(20000)


def knapsack(num_item, size, items):
    """Given the knapsack size, number of items, and the items(in form of
    [[item_value, item_size]]), compute the optimal value of the items that
    fit in knapsack. Top-down(recursive) version"""

    cache = {}
    def pack(nItem, limit):
        if (nItem, limit) not in cache:
            if nItem == 0:
                cache[(nItem, limit)] = 0
            elif items[nItem][1] > limit:
                cache[(nItem, limit)] = pack(nItem - 1, limit)
            else:
                cache[(nItem, limit)] = max(pack(nItem - 1, limit),
                        pack(nItem - 1, limit - items[nItem][1]) +
                            items[nItem][0])
        return cache[(nItem, limit)]
    return pack(num_item, size)


def main():
    items = [[0,0]]
    size, num_item = map(int, open('knapsack_big.txt').readline().strip().split(' '))
    #size, num_item = map(int, open('test_big.txt').readline().strip().split(' '))
    with open('knapsack_big.txt') as file_in:
    #with open('test_big.txt') as file_in:
        next(file_in)
        for line in file_in:
            items.append(map(int, line.strip().split(' ')))
    start = time.time()
    print knapsack(num_item, size, items)
    print time.time() - start


if __name__ == "__main__":
    main()
