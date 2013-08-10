import bisect
from time import time


def two_sum(array):
    """Returns the numbers from [-WIDTH, WIDTH] that can be obtained by
    summing up any two elements in 'array'."""

    WIDTH = 10000
    out = set()
    for i in array:
        lower = bisect.bisect_left(array, -WIDTH - i)
        upper = bisect.bisect_right(array, WIDTH - i)
        out |= set([i + j for j in array[lower:upper]])
    return out


def main():
    array = []
    with open('algo1_programming_prob_2sum.txt') as file_in:
        for line in file_in:
            num = int(line.strip())
            array.append(num)
    array.sort()
    return len(two_sum(array))


if __name__ == '__main__':
    start = time()
    print main()
    print time() - start
