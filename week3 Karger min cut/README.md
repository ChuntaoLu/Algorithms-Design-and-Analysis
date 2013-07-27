#<center>Algo week 3: Karger min cut </center>
***
It is week three for the Algorithms course, and the main topic is the Karger minimum cut problem for an undirected graph. The Karger algo itself is clean and neat, however it can also be cumbersome to implement for me who lacks good understanding of data structures. I spent some pre-work to figure out what would be the best choice to represent the graph, or adjacency list. My gut feeling is dictionary would work but not beautifully. I decide to construct a class to implement the graph for two reasons: make things neat and practice with class. I try to follow PEP8 and code with less comments in a sense that the style should make the codes easily readable.

The running time with just one iteration of `cut` is about 0.04 secs, which is pretty slow considering that *n&times;nln(n)* iterations are needed to achieve *1/n* error probability. Although it actually runs fairly less number of trials to get a correct answer, I think there is still a lot to improve. And something worth pointing out is that `deepcopy` is a must before performing any cut in order to have the same fresh graph every time. For the class object I have here `deepcopy` takes tenth of the running time.

<small>Note: My code doesn’t truly randomly select an edge, instead it first randomly select a node then randomly select one of its edges. Though it works, the right way to uniformly randomly select an edge is to choose one from all the edges.
</small>
