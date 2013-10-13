import scc
from time import time
from collections import defaultdict


def two_sat(graph):
    """
    Given a 2SAT problem represented by a directed graph in forms of 
    {tail:[head_list], ...}, compute the satisfiability.

    
    Below symbol 'v' means 'or', '^' means 'and', '<=>' means 'equivalent to',
    '-' means 'negate', and '->' means material implication.

    A 2SAT problem in CNF, which is (x1 v x2)^(x1 v x3)^(x2 v x3)..., can be
    represented by an implication graph by replacing each of its disjunctions
    by a pair of material implications. It is satisfiable if and only if no
    vertex and its negation belong to the same SCC (strongly connected component)
    of the implication graph. SCC can be computed in linear time O(m + n), where
    m is the number of the edges of the graph and n is the number of nodes.

    Equivalence between boolean clause and material implication:
    (x1 v x2) <=> (-x1 -> x2) <=> (-x2 -> x1)

    An implication graph is constructed by adding edges (-x1, x2) and (-x2, x1)
    for each disjunction (x1 v x2). Despite the equivalence between the boolean 
    clause and EACH material implication, BOTH edges must be added to the graph
    in order for the edges to be able to represent the relation of vertices.

    If x and -x are both in the same SCC, which implies (-x -> x) ^ (x -> -x),
    then a contradiction is concluded as below:

    (-x -> x) <=> (x v x) <=> x
    (x -> -x) <=> (-x v -x) <=> -x
    thus, (-x v x) ^ (x -> -x) <=> (x ^ -x) <=> False

    https://class.coursera.org/algo2-002/forum/thread?thread_id=428#post-1573
    https://class.coursera.org/algo2-002/forum/thread?thread_id=428#comment-1584
    """

    groups = scc.scc(graph)
    for group in groups.values():
        group = set(group)
        for node in group:
            if -node in group:
                return 0
    return 1


def main():
    out = []
    for i in range(1, 7):
        graph = defaultdict(list)
        with open("2sat%s.txt" % i) as file_in:
            next(file_in)
            for line in file_in:
                x1, x2 = map(int, line.strip().split(' '))
                graph[-x1].append(x2)
                graph[-x2].append(x1)
        out.append(two_sat(graph))
        del graph
    return out


if __name__ == "__main__":
    start = time()
    print main()
    print time() - start
