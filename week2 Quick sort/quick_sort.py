import time


def quick_sort(array):
    """
    Returns a sorted 'array' by quick sort algorithm via list comprehension,
    here 'array' is actually a list.
    """

    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = quick_sort([x for x in array[1:] if x < pivot])
        right = quick_sort([x for x in array[1:] if x >= pivot])
        return left + [pivot] + right


def main():
    start_time = time.time()
    input_file = open('QuickSort.txt').read().strip().split()
    array = [int(i) for i in input_file]
    sorted_array = quick_sort(array)
    print time.time() - start_time

if __name__ == '__main__':
    main()
