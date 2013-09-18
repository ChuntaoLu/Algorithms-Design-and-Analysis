def cluster(num_clusters, desired_num_clusters, sorted_edges, nodes_set):
    """Given 'sorted_edges' as lists of [head, tail, edge_dist] sorted
    by edge_dist in increasing order, and the 'nodes_set' as dicts of 
    {node: [parent, rank]}, compute a max-spacing 'desired_num_clusters'
    clustering out of 'num_clusters' single nodes. Algorithm is based on 
    Kruskal's minimum spanning tree algorithm."""


    while num_clusters > desired_num_clusters:
        node_a, node_b, edge_dist = sorted_edges.pop(0)
        while same_root(node_a, node_b, nodes_set): 
            node_a, node_b, edge_dist = sorted_edges.pop(0)
        union(node_a, node_b, nodes_set)
        num_clusters -= 1
    node_a, node_b, edge_dist = sorted_edges.pop(0)
    while same_root(node_a, node_b, nodes_set): 
        node_a, node_b, edge_dist = sorted_edges.pop(0)
    return node_a, node_b, edge_dist


def same_root(node_a, node_b, nodes_set):
    """Returns True if two nodes have the same root."""

    a_root = find_set(node_a, nodes_set)
    b_root = find_set(node_b, nodes_set)
    return a_root == b_root

def union(node_a, node_b, nodes_set):
    """Union two nodes or the clusters they belong to."""

    a_root = find_set(node_a, nodes_set)
    b_root = find_set(node_b, nodes_set)
    link(a_root, b_root, nodes_set)


def link(node_x, node_y, nodes_set):
    """Union by rank, node with lower rank added to the one with
    higher rank; arbitrarily union if two nodes have same rank."""

    if nodes_set[node_x][1] > nodes_set[node_y][1]:
        nodes_set[node_y][0] = node_x
    else:
        nodes_set[node_x][0] = node_y
        if nodes_set[node_x][1] == nodes_set[node_y][1]:
            nodes_set[node_y][1] += 1


def find_set(node, nodes_set):
    """Recursively find the root of a node."""

    if node != nodes_set[node][0]:
        nodes_set[node][0] = find_set(nodes_set[node][0], nodes_set)
    return nodes_set[node][0]


def make_nodes_set(num_nodes):
    """Initialize 'nodes_set' where a node's parent is itself and
    rank is 0."""

    return dict([[i, [i, 0]] for i in range(1, num_nodes + 1)])


def main():
    edges = []
    #with open('test.txt') as file_in:
    with open('clustering1.txt') as file_in:
        next(file_in)
        for line in file_in:
            edges.append(map(int, line.strip().split(' ')))
    sorted_edges = sorted(edges, key = lambda edge: edge[-1])
    #num_clusters = int(open('test.txt').readline().strip())
    num_clusters = int(open('clustering1.txt').readline().strip())
    desired_num_clusters = 4
    nodes_set = make_nodes_set(num_clusters)
    return cluster(num_clusters, desired_num_clusters, sorted_edges, nodes_set)

if __name__ == '__main__':
    print main()
