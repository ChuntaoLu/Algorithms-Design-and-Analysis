#This script computes the strong connected components(SCC) of a given graph.
import sys
import time
import resource
from itertools import groupby
from collections import defaultdict


#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


class Track(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes."""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()


def dfs(graph_dict, node, track):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail node: [head nodes]}. Depth first search runs recrusively and keeps
    track of the parameters"""

    track.explored.add(node)
    track.leader[node] = track.current_source
    for head in graph_dict[node]:
        if head not in track.explored:
            dfs(graph_dict, head, track)
    track.current_time += 1
    track.finish_time[node] = track.current_time


def dfs_loop(graph_dict, nodes, track):
    """Outter loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""

    for node in nodes:
        if node not in track.explored:
            track.current_source = node
            dfs(graph_dict, node, track)


def scc(graph, reverse_graph, nodes):
    """First runs dfs_loop on reversed graph with nodes in decreasing order,
    then runs dfs_loop on orignial graph with nodes in decreasing finish
    time order(obatined from firt run). Return a dict of {leader: SCC}."""

    out = defaultdict(list)
    track = Track()
    dfs_loop(reverse_graph, nodes, track)
    sorted_nodes = sorted(track.finish_time,
                          key=track.finish_time.get, reverse=True)
    track.current_time = 0
    track.current_source = None
    track.explored = set()
    dfs_loop(graph, sorted_nodes, track)
    for lead, vertex in groupby(sorted(track.leader, key=track.leader.get),
                                key=track.leader.get):
        out[lead] = list(vertex)
    return out


def main():
    start = time.time()
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    nodes = set()
    with open('SCC.txt') as file_in:
    #with open('test.txt') as file_in:
        for line in file_in:
            x = line.strip().split()
            x1, x2 = int(x[0]), int(x[1])
            nodes |= set([x1, x2])
            graph[x1].append(x2)
            reverse_graph[x2].append(x1)
    nodes = sorted(list(nodes), reverse=True)
    t1 = time.time() - start
    print t1
    groups = scc(graph, reverse_graph, nodes)
    t2 = time.time() - start
    print t2
    sorted_groups = sorted(groups, key=lambda x: len(groups[x]), reverse=True)
    result = []
    for i in range(5):
        try:
            result.append(len(groups[sorted_groups[i]]))
        except:
            result.append(0)
    return result


if __name__ == '__main__':
    print main()
