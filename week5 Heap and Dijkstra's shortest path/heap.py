import heapq
from heapq_showtree import show_tree


def bubble_up(array, index):
    """Keep heap invariant when new item appended"""

    parent_index = (index - 1) // 2
    if index == 0 or array[index] >= array[parent_index]:
        return
    else:
        array[parent_index], array[index] = array[index], array[parent_index]
        bubble_up(array, parent_index)


def bubble_down(array, index):
    """Keep heap invariant when heap top popped"""

    try:
        child_index = array.index(min(array[index * 2 + 1],
                                      array[index * 2 + 2]))
    except:
        if index * 2 + 2 == len(array):
            child_index = len(array) - 1
        else:
            return
    if array[index] <= array[child_index]:
        return
    else:
        array[child_index], array[index] = array[index], array[child_index]
        bubble_down(array, child_index)


def heap_insert(heap, item):
    """Equivalent to heapq.heappush(heap, item)"""

    heap.append(item)
    bubble_up(heap, len(heap) - 1)


def heap_extract(heap):
    """Equivalent to heapq.heappop(heap)"""

    heap[0], heap[-1] = heap[-1], heap[0]
    out = heap.pop()
    if len(heap):
        bubble_down(heap, 0)
    return out


def list_to_min_heap(array):
    """Equivalent to heapq.heapify(array) except in-place"""

    out = []
    for i in array:
        heap_insert(out, i)
    return out


def heap_sort(array):
    """Equivalent to sorted(array)"""

    heap = list_to_min_heap(array)
    out = [heap_extract(heap) for i in range(len(array))]
    return out


def main():
    """test"""

    test = [6, 5, 3, 1, 8, 7, 2, 4]
    heap = list_to_min_heap(test)
    show_tree(heap)
    heapq.heapify(test)
    show_tree(test)
    print test
    #print heap_sort(test)


if __name__ == '__main__':
    main()
