#<center>Algo week 4: Graph search and Kosaraju SSC finder </center>
***
Breath First Search(BFS) and Depth First Search(DFS) are the basics of graph search, which I actually learned about before from [edx](http://www.edx.org)’s popular AI course. That’s when I started to check out what computer science could be. I was taking another popular edx course(MIT’s intro to CS and Programming) at the same time, which was good because the course level matched my weak background. But the AI course was just beyond my scope, with no surprise I struggled a lot and I still remember hours and hours me staring at the code and Googling around trying to make sense everything. What I am proud of is at the end I managed to finish the course with a final grade of 94%. I should probably had taken that course some time later and I could be more efficient. But that achievement was huge for me at that time and it was definitely one of the indispensables that drive me go deeper into CS.

BFS explores the nodes in layers, so it is capable of finding the shortest path from the source node to a certain node. And for undirected graph, it can also compute all connected components. DFS aggressively goes deep into a branch until it reaches an end then backtracks to shallow nodes. It is good at finding topological ordering of a directed acyclic graph and connected components in directed graphs. Despite of the different search behaviors, BFS and DFS are almost the same code wise, the only difference is BFS stores nodes in a queue(FILO) while DFS uses a stack(FIFO). Both algorithms have a linear running time of *O(m+n)*, where *m* is the number of edges and *n* is number of nodes. While BFS and DFS can be implemented iteratively, DFS could also be done in a slicker recursive way. That being said, the star of this weak is Kosaraju’s two pass algorithm for computing strongly connected components(SCC). I didn’t grasp the idea of the algo when I watched the video, and to be honest even after I successfully implemented the algo I still wonder why it works. The algo itself is not hard:

1. Create a reversed graph with all arches reversed.
2. Run DFS loop on the reversed graph to compute the finishing time of each node.
3. Run DFS loop on the original loop processing the nodes in decreasing order of finishing times.

The SSCs are the nodes with the same leaders(the biggest node number in the group). The DFS loop is very neat, what might be confusing is to track all the stuff: current time, current source node, leader, finishing time and the explored nodes. These variables need to be global in the sense of tracking, however the rule of thumb for Python is to stay away from globals. So I put everything into a Track class, being instance attributes they are safe and easy to handle. Recursion tracks the finishing time of each node beautifully and painlessly. I tried the iterative approach and my way of time tracking was just ugly. There must be a better way handling time tracking iteratively, but who doesn’t like recursion anyway? However, because of the huge size of graph, and Python’s default recursion limit setting, you will probably certainly encounter the “maximum recursion depth reached” error. Fear not, just push the recursion limit and also increasing the stack size as below:

```python
import sys
import resource
 

#only works for Linux
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
```
