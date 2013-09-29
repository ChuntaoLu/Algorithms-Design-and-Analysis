import time


def Floyed_Warshall(num_nodes, edges):
    """Given the graph nodes(labeled from 1 to 'num_nodes') and the graph edges
    (in form of {(tail, head): edge_dist}), computes the all pairs shortest
    path if graph does not contain negative cycle.

    'current_array[i][j]' and 'last_array[i][j]' keep track of the shortest path
    with 'k' edges and 'k - 1' edges respectively. Since both arrays actually point
    to the same array, when 'current_array[i][j]' gets updated, so does 'last_array
    [i][j]'.

    In any iteration k, 'current_array[i][i] < 0' detects a negative cycle.

    Running time of O(n*n*n) where n is number of nodes in graph."""

    inf = float('inf')
    bound = num_nodes + 1
    current_array = [[inf for j in range(bound)] for i in range(bound)] 
    #no need to do value swap, OK to have both point to same array
    #whenever 'current_array' updated, so does 'last_array'
    last_array = current_array
    for i in range(bound):
        for j in range(bound):
            if i == j:
                last_array[i][j] = 0
            elif (i, j) in edges:
                last_array[i][j] = edges[(i,j)]
    for k in range(1, bound):
        for i in range(1, bound):
            for j in range(1, bound):
                current_array[i][j] = min(last_array[i][j],
                        last_array[i][k] + last_array[k][j])
                if i == j:
                    if current_array[i][j] < 0:
                        return "Graph has negative cycle!" 
    return min(min(current_array, key=lambda x: min(x)))
    

def main():
    #files = ['test.txt']
    files = ['g1.txt', 'g2.txt', 'g3.txt']
    for file_name in files:
        edges = {}
        with open(file_name) as file_in:
            next(file_in)
            for line in file_in:
                tail, head, dist = map(int, line.strip().split(' '))
                edges[(tail, head)] = dist
        num_nodes = int(open(file_name).readline().strip().split(' ')[0])
        start = time.time()
        print Floyed_Warshall(num_nodes, edges)
        print time.time() - start


if __name__ == '__main__':
    main()

