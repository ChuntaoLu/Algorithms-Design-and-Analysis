def merge_2d(a, b, axis = 0):
    '''function to merge 2 sorted list, 'a' and 'b' are lists of 2-tuples.
    'axis' is the coordinate which sort is based on, defalut as x axis.'''

    i ,j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if a[i][axis] < b[j][axis]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:]
    c += b[j:]
    return c

def merge_sort_2d(seq, axis = 0):
    '''recursive function to merge and sort'''

    if len(seq) == 1:
        return seq
    else:
        mid = int(len(seq)/2)
        head = merge_sort_2d(seq[:mid], axis)
        end = merge_sort_2d(seq[mid:], axis)
        return merge_2d(head, end, axis)

#test cases
#print merge_sort_2d([(1,9),(45,6),(7,25),(89,9),(76,39),(63,86),(0,37)])
#print merge_sort_2d([(1,9),(45,6),(7,25),(89,9),(76,39),(63,86),(0,37)], 1)
#print merge_sort_2d([(2,1),(0,3),(6,9)])
#print merge_sort_2d([(2,1),(0,3),(6,9)], 1)
#print merge_sort_2d([(2,1),(0,3)])
#print merge_sort_2d([(2,1),(0,3)], 1)
#print merge_sort_2d([(2,1)])
