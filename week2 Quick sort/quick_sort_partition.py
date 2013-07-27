import time


def element_swap(array, index1, index2):
    '''Swap the two elements with index1 and index2 in an array.'''

    array[index1], array[index2] = array[index2], array[index1]


def partition_head(array, head, tail):
    """
    Partations an 'array' with its first element as 'pivot'.
    Returns the final index of the pivot.

    head: the index where partition starts.

    tail: the index where patition ends.

    pointer: initially points to the element immediately after head, increases
    by one after every swap during comparison, always points to the element
    that starts the right half, if no element on right half emerged yet, points
    to the last of the left half. Eventually points to the final index of pivot
    + 1.

    During comparison, swap only happens when element is smaller than pivot,
    swap like array[0], array[0] == array[0], array[0] is allowable. The final
    swap is bwteen pivot and the last element of left half.
    """

    pivot = array[head]
    pointer = head + 1
    for index in range(head+1, tail):
        if array[index] < pivot:
            element_swap(array, pointer, index)
            pointer += 1
    element_swap(array, pointer - 1, head)
    return pointer - 1


def quick_sort(array, head, tail):
    if tail - head <= 1:
        return
    else:
        pivot = partition_head(array, head, tail)
        quick_sort(array, head, pivot)
        quick_sort(array, pivot+1, tail)


def main():
    start_time = time.time()
    input_file = open('QuickSort.txt').read().strip().split()
    array = [int(i) for i in input_file]
    quick_sort(array, 0, len(array))
    print time.time() - start_time

if __name__ == '__main__':
    main()
