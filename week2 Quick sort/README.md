#Algo week 2: Quick sort
***
This week’s Algorithms course focused on Quick sort, which is a very clever and neat sorting algorithm. The core idea of Quick sort is really simple, find a pivot, put smaller elements on its left and bigger ones on its right, recursively do this with the left and right halves then it’s done. The only thing that could be tricky is how to place the left and right. [Tim Roughgardon](http://theory.stanford.edu/~tim/) did an excellent job explaining ‘partition’. It starts by taking one element of a n element list as ‘pivot’, then compares the rest elements with the pivot and does some swaps, after which all the smaller elements are on the left of the pivot and those equal and bigger ones on the right. This procedure only involves *n-1* comparisons. Complexity analysis shows the average running time of Quick sort is *nlogn*, given the pivot is chosen randomly. 

Quick sort becomes sweeter to implement in Python if we ignore partition, in which case *2(n-1)* comparisons are involved instead of *n-1*. One would expect it will be less efficient due to more comparisons, but it turns out the opposite when Quick sort is implement with Python's list comprehension. Reason is list comprehension is so well optimized(by C loop) that it takes way less time than general for loops.

###Scripts include:

1. Quick sort with partition
2. Quick sort without partition
