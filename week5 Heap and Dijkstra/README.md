Algo week #5 Heap and Dijkstra's shortest path
--------------------

This week's content is rich, it covers Dijksrta's shortest path algorithm and several data structure, among which heap is emphasized.

Heap is a tree data structure whose parent-child order pattern is always the same, namely a parent node is always either bigger or smaller than its children, which leads to a max heap or a min heap. A binary heap has no more than two child nodes for each node. As a specific data structure, heap is also referred to priority queue, an abstract data structure. The typical operations of heap (without breaking the invariant) includes:

+ Insert: add new object, running time *O(logn)*
+ Extract-Min: remove the top element, running time *O(logn)*
+ Heapify: batch insertion to build heap, running time *O(n)*

While all this operations can be implemented using swaps, bubble ups and bubble downs, Python has a library `heapq` for heap, and above operations are easily fulfilled by `heappush()`, `heappop()` and `heapify()`. The most simple heap could be a heapified list containing integers. With the property of heap, heap sort kicks in naturally: heapify a given list and repeatly extract min. More efficient use of heap is priority queue which usually contains tuples in form of (priority, node). A priority queue should also be capable of following operations (without breaking invariant):

+ Insert with priority: add new or update an existing object with desired priority
+ Delete: remove any arbitrary object from the queue

Although Python's `heapq` library does not support such operations, it gives a neat [demonstration](http://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes) on how to implement them, which is a slick trick and works like a charm. 

Dijkstra's shortest path algorithm is very fairly intuitive:

1. Initialize the passed nodes with the source and current shortest path with zero.
2. Include the node that minimize the current shortest path plus the edge distance among all edges whose tail are in the passed nodes and head in uncharted nodes.
3. Update the current shortest path and repeat step 2 until all nodes are passed.

Basically, the whole algorithm is just one loop, it can be implemented naively with running time *O(mn)*, where *m* and *n* are number of edges and nodes. It's quadratic and picking the right node could be very clumsy. However, with the right data structure, a priority queue, picking the right node is just as simple as extracting the minimum (the hard part is to update priorities while maintaining invariant, but it's already demoed!), and boom the running time reduces to *O(mlogn)*.

####scripts include:

1. Heap operations and heap sort
2. Priority queue and Dijkstra's algorithm
3. Pretty print a tree from [PyMOTW](http://pymotw.com/2/heapq/index.html)    