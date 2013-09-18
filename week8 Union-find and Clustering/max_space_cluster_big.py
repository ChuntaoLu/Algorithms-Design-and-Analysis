def cluster(num_clusters, nodes_set):
    """Given implicit edge costs and the 'nodes_set' as dicts of {node: [parent, rank]},
    compute the largest value of 'num_clusters' so that the clustering has spacing at 
    least 3 bit flips"""
    all_nodes = set(nodes_set.keys())
    for node in all_nodes:
        possible_nodes = two_bit_flip(node)
        actual_nodes = possible_nodes.intersection(all_nodes)
        for other_node in actual_nodes:
            if not same_root(node, other_node, nodes_set):
                union(node, other_node, nodes_set)
                num_clusters -= 1
    return num_clusters


def two_bit_flip(node):
    """Give all the nodes by flipping one or two bits of the binary number
    representation of a node.""" 

    node_list = list(node)
    out = set()
    bit_length = len(node_list)
    for i in range(bit_length):
        for j in range(bit_length):
            new_node = node_list[:]
            if i != j:
                new_node[i] = ('1' if node[i] == '0' else '0')
                new_node[j] = ('1' if node[j] == '0' else '0')
            else:
                new_node[i] = ('1' if node[i] == '0' else '0')
            out.add(''.join(new_node))
    return out


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


def main():
    nodes_set = {}
    with open('test_big.txt') as file_in:
    #with open('clustering_big.txt') as file_in:
        next(file_in)
        for line in file_in:
            node = ''.join(line.strip().split(' '))
            nodes_set[node] = [node, 0]  
    #node ids in input file have duplicates
    num_clusters = len(nodes_set)
    return cluster(num_clusters, nodes_set)

if __name__ == '__main__':
    print main()
