def merge(a, b):
    '''function to merge 2 sorted list'''

    i ,j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:]
    c += b[j:]
    return c

#alternative way for merge function
#def merge(a, b):
#    '''function to merge 2 sorted list'''
#
#    a.append(float('inf')) #add infinite max to avoid index issue
#    b.append(float('inf'))
#    i ,j = 0, 0
#    c = []
#    for k in range(len(a)+len(b)-2):
#        if a[i] < b[j]:
#            c.append(a[i])
#            i += 1
#        else:
#            c.append(b[j])
#            j += 1
#    return c


def merge_sort(seq):
    '''recursive function to merge and sort'''

    if len(seq) == 1:
        return seq
    else:
        mid = int(len(seq)/2)
        head = merge_sort(seq[:mid])
        end = merge_sort(seq[mid:])
        return merge(head, end)

#test cases
#print merge_sort([1,45,6,7,25,89,9,76,39,63,86,37])
#print merge_sort([2,1,5,3])
#print merge_sort([2,1,5])
#print merge_sort([2])
#print merge_sort([2,1])

