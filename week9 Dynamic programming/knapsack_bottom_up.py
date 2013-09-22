def knapsack(num_item, size, items):
    """Given the knapsack size, number of items, and the items(in form of
    [[item_value, item_size]]), compute the optimal value of the items that
    fit in knapsack."""

    #'array' keeps track of the optimal subproblem solutions
    array = [[None for i in range(size + 1)] for j in range(num_item + 1)]
    #initialize 'array', optimal value always 0 when there is no item.
    for i in range(size + 1):
        array[0][i] = 0

    for i in range(1,num_item + 1):
        for j in range(size + 1):
            if items[i][1] > j: #item size bigger than knapsack size
                array[i][j] = array[i - 1][j]
            else:
                array[i][j] = max(array[i-1][j], array[i-1][j - items[i][1]] + items[i][0])
    return array[num_item][size]


def main():
    items = [[0,0]]
    size, num_item = map(int, open('knapsack1.txt').readline().strip().split(' '))
    #size, num_item = map(int, open('test.txt').readline().strip().split(' '))
    with open('knapsack1.txt') as file_in:
    #with open('test.txt') as file_in:
        next(file_in)
        for line in file_in:
            items.append(map(int, line.strip().split(' ')))
    return knapsack(num_item, size, items)


if __name__ == "__main__":
    print main()
