Algo week 6: Hash table and Bloom filter
------------------------

It’s the end of the Algo part 1, and the topic is largely hash table, one of the most important data structures. Hash table is probably not something new if one has ever fiddled around any programming language. Because of the amazing lookup speed *O(1)*, almost every language has its own build-in hash table, such as `dict` for Python, `hash` for Ruby, etc. Essentially, hash tables are key-value pairs, while the concept may looks simple on the surface, it is actually pretty complicated under the hood. A good hash table implementation mainly depends on a good hash function which should be fast to evaluate and capable of spreading data out randomly and uniformly into ‘buckets’. One necessary condition of a hash table is the load factor(number of objects over number of buckets) need to be *O(1)*. And some basic rules for choosing number of buckets:

1. Choose n to be a prime
2. Not close to a power of 2
3. not close to a power of 10

An ideal hash function would avoid any possible collisions so that any distinct data would have distinct keys. However, such a hash function does not exist, because no matter what hash function you come up with there always exists a pathological data set. Typical solution to this problem is to design a family of hash functions, almost all of which spread out data pretty evenly, and then randomly choose hash functions from that family. By doing so, the collision potability is managed less than *1/n*, where n is number of buckets. And functions in that family are ‘universal’ hash functions.

A bloom filter utilizes universal hash functions to achieve fast insertions and lookups with high space efficiency and yet not a hash table in senses that it doesn’t actually store any object, no deletions are supported, and furthermore there exists small false positive probability. Bloom filter works as follows:

+ Use a n bits array A to store existence status.
+ Use k hash functions for object-existence pair mapping.
+ Insertion: set A[h<sub>i</sub>(x)] = 1 for i = 1,2,...,k regardless previous bit value.
+ Lookup: object exists if A[h<sub>i</sub>(x)] = 1 for all i = 1,2,...,k.

Bloom filter has no false negatives: if an object is previously inserted, a lookup will always confirm its existence. However, since there are chances that bits for new insertion might have been set to 1 by previous insertions, false positives are possible. Luckily, because of the good choices of universal hash functions, the probability of false positives is less than 1-e<sup>(-k/b)</sup>, where b is number of bits per object. To illustrate, with b=8, k=5, the error probability is only about 2%.

There are two homework problems this week: one is (arguably) about hash table, and the other is about heap (from last week). I say the first problem is arguably about hash table because it can be solved more naturally without thinking about hashing. To be honest, I got stuck when I tried too hard focusing on a hash table approach without analyzing the problem. For a single 2sum problem, with each number in a number set(python’s set is a hash table), looking up its corresponding part cost *O(1)* time, and linear time is required to traverse the set, which is not bad. Things become interesting when we have more than a single 2sum problem, say 10,000. This means 10,000 lookups per number in the set, namely billions of lookups if the set has a size of million. The point is that lookup is still fast but we just got plain too many of them. The trick is to observe the features of the 2sum problem, in the homework 2sum is desired in a range of `[-10000, 10000]`, which is rather a small range compared to the randomly large numbers in the txt file. So instead of hashing, simply sort the numbers as a list, and for each number i decide a window `[-10000-i, 10000-i]`, then find the numbers in that window using the excellent `bisect` module. It’s done in several seconds. One can also build customized has table with bucket size of the range width, and then do the same window trick to solve the problem quickly. However, it is not faster and actually a bit clumsy compared to bisect approach. Note that the window trick works simply because the 2sum range is small and numbers in the file are large and uniformly distributed, if the window size is close to the scale of numbers in the file then it would fail. I guess there might be better hash table approaches when window blows, but I doubt it can be easily grasped. 

The second problem is to main medians for a streamed number list. The idea for this problem is to have two heaps: a heap_lo as a max_heap to store the smaller half of received numbers with its maximum as top node, a heap_hi as a min_heap to store the bigger half with its minimum as top node. With this setup, when a new number is received one just check against the top nodes of heap_lo and heap_hi, and insert in the proper heap. To keep the two heaps balanced, pop the top node from the longer heap and insert it into the shorter heap. The median is always one of the top nodes from heap_lo and heap_hi. So the key is to have two types of heaps, unfortunately python’s heapq module only supports min_heap. Fear not, heap is actually not hard to implement, here is my implementation of heap which support both max_heap and min_heap. Once you have the right heaps, maintaining medians is simple.

####scripts include:

1. Heap that supports both max_heap and min_heap
2. 2sum solution with bisect approach
3. Median maintenance with double heaps 
3. Pretty print a tree from [PyMOTW](http://pymotw.com/2/heapq/index.html) 