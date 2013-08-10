import heapq
from heapq_showtree import show_tree


def bubble_up(array, index, kind):
    """Keep heap invariant when new item appended"""

    parent_index = (index - 1) // 2
    option = {'min': '>', 'max': '<'}
    min_or_max = 'array[index] %s= array[parent_index]' % option[kind]
    if index == 0 or eval(min_or_max):
        return
    else:
        array[parent_index], array[index] = array[index], array[parent_index]
        bubble_up(array, parent_index, kind)


def bubble_down(array, index, kind):
    """Keep heap invariant when heap top popped"""

    option = {'min': '<', 'max': '>'}
    min_or_max = 'array[index] %s= array[child_index]' % option[kind]
    try:
        child_index = array.index(eval(
            '%s(array[index * 2 + 1], array[index * 2 + 2])' % kind))
    except:
        if index * 2 + 2 == len(array):
            child_index = len(array) - 1
        else:
            return
    if eval(min_or_max):
        return
    else:
        array[child_index], array[index] = array[index], array[child_index]
        bubble_down(array, child_index, kind)


def heap_insert(heap, item, kind):
    """Equivalent to heapq.heappush(heap, item)"""

    heap.append(item)
    bubble_up(heap, len(heap) - 1, kind)


def heap_extract(heap, kind):
    """Equivalent to heapq.heappop(heap)"""

    heap[0], heap[-1] = heap[-1], heap[0]
    out = heap.pop()
    if len(heap):
        bubble_down(heap, 0, kind)
    return out


def list_to_heap(array, kind='min'):
    """Equivalent to heapq.heapify(array) except in-place"""

    out = []
    for i in array:
        heap_insert(out, i, kind)
    return out


def heap_sort(array, kind):
    """Equivalent to sorted(array)"""

    heap = list_to_heap(array, kind)
    out = [heap_extract(heap, kind) for i in range(len(array))]
    return out


def main():
    """test"""

    test = [6, 5, 3, 1, 8, 7, 2, 4]
    heap = list_to_heap(test, 'min')
    show_tree(heap)
    heapq.heapify(test)
    show_tree(test)
    print heap
    print test
    print heap_sort(test, 'max')
    print heap_sort(test, 'min')


if __name__ == '__main__':
    main()
