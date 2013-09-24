def knapsack(num_item, size, items):
    """Given the knapsack size, number of items, and the items(in form of
    [[item_value, item_size]]), compute the optimal value of the items that
    fit in knapsack.

    By observing our dynamic programming recurrence,
    
    A[i,x]=max{A[i-1,x],A[i-1,x-wi]+vi}
    
    It is easy to see that we only need A[i-1,*], instead of the whole 2D-array
    A, to compute A[i,*]. Thus we can maintain only TWO arrays: one (array A)
    for caching the result in the previous step, and the other (array B) for the 
    current step computation. So the recurrence becomes
    
    B[x]=max{A[x],A[x-wi]+vi}
    
    And we swap A and B before the next iteration step.
    
    Even trickier, we can actually maintain only ONE array! The trick is to scan
    the array in reversing order, i.e., from big end to small end. In other words,
    we do the computation from big knapsack size to small knapsack size.
    
    A[x]=max{A[x],A[x-wi]+vi}
    
    The reason is that A[x] is updated by either unchanging or using A[x-wi] which
    represents smaller knapsack size than x. Consequently, by such reversed scan,
    you will never erase your previous result."""

    #'array' keeps track of the optimal subproblem solutions only for previous 
    #knapsack size. Initialize 'array', optimal value always 0 when there is no item.
    array = [0 for i in range(size + 1)]
    for i in range(1,num_item + 1):
        for j in range(size, 0, -1):
            if items[i][1] <= j: #item size bigger than knapsack size
                array[j] = max(array[j], array[j - items[i][1]] + items[i][0])
    return array[size]


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
