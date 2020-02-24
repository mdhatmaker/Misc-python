import sys

# https://practice.geeksforgeeks.org/problems/geek-collects-the-balls/0
# https://www.geeksforgeeks.org/graph-and-its-representations/

# There are two parallel roads, each containing N and M buckets, respectively. Each
# bucket may contain some balls. The buckets on both roads are kept in such a way that
# they are sorted according to the number of balls in them. Geek starts from the end
# of the road which has the bucket with a lower number of balls (i.e. if buckets are
# sorted in increasing order, then geek will start from the left side of the road).
# The geek can change the road only at the point of intersection (which means, buckets
# with the same number of balls on two roads). Now you need to help Geek to collect
# the maximum number of balls.

###############################################################################


# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
  
# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the # of the vertices (V).
class GraphAdjList: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
  
    def add_edges(self, edge_list):
        for e in edge_list:
            self.add_edge(e[0], e[1])

    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}:  head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print() 
  

# A class to represent a graph as an adjacency matrix.
class GraphAdjMatrix:
    def __init__(self, V, vertex_set):      # V is vertex count; M is 2D matrix
        self.vertex_map = {}                # vertex_map maps vertex key to vertex number
        for i,x in enumerate(vertex_set):
            self.vertex_map[x] = i
            #print('map:', x, '->', i)
        self.V = V
        self.M = [0] * V
        for i in range(V):
            self.M[i] = [0] * V

    def __repr__(self):
        s = str(self.M[0])
        for i in range(1, self.V):
            s = s + '\n' + str(self.M[i])
        return s

    def get(self, i, j):
        xi = self.vertex_map[i]
        xj = self.vertex_map[j]
        return self.M[xi][xj]

    def set(self, i, j, value):
        xi = self.vertex_map[i]
        xj = self.vertex_map[j]
        self.M[xi][xj] = value

    def add_directed_edge(self, i, j, weight=1):
        xi = self.vertex_map[i]
        xj = self.vertex_map[j]
        self.M[xi][xj] = weight

    def add_edge(self, i, j, weight=1):
        xi = self.vertex_map[i]
        xj = self.vertex_map[j]
        self.M[xi][xj] = weight
        self.M[xj][xi] = weight

    def add_edges(self, edge_list):
        for e in edge_list:
            self.add_edge(e[0], e[1])

    def get_edges(self, i):
        xi = self.vertex_map[i]
        edges = []
        for j in self.vertex_map:   # range(self.V):
            xj = self.vertex_map[j]
            #print('j/xj:', j, xj)
            if self.M[xi][xj] > 0:
                edges.append((i, j, self.M[xi][xj]))
        return edges
    

# given GraphAdjMatrix, perform a topological sort based on depth-first search
def graph_dfs(g):
    L = []          # empty list that will contain the sorted nodes
    marked_nodes = {}
    for v in g.vertex_map:
        marked_nodes[v] = 0     # 0 = unmarked; 1 = temporary mark; 2 = permanent mark
    #print('\n', marked_nodes)
    while sum(marked_nodes.values()) < 2*len(marked_nodes):  # while exists nodes without a permanent mark
        for n in marked_nodes:
            if marked_nodes[n] < 2: break
        visit(g, n, marked_nodes, L)
    print('\n', L)

def visit(g, n, marked_nodes, L):
    print('visit:', n, end='   ')
    if marked_nodes[n] == 2: return     # if node has permanent mark, then return
    if marked_nodes[n] == 1: pass       # if node has temporary mark, then stop (not a DAG)
    marked_nodes[n] = 1
    edges = g.get_edges(n)              # find each node m with an edge from n to m
    """print(edges)
    for e in edges:
        print('edge:', (e[0], e[1]), end=' ')
    print()"""
    marked_nodes[n] = 2                 # remove temporary mark from n and mark n with permanent mark
    #L.insert(0, n)                      # add n to head of L
    L.append(n)

    


def dijkstras_shortest_path():
    nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    distances = {
        'B': {'A': 5, 'D': 1, 'G': 2},
        'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'G': {'B': 2, 'D': 1, 'C': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
        'F': {'A': 5, 'E': 2, 'C': 16}}
    # expected output:  {'E': 2, 'D': 1, 'G': 2, 'F': 4, 'A': 4, 'C': 3, 'B': 0}
    #   actual output:  {'B': 0, 'D': 1, 'E': 2, 'G': 2, 'C': 3, 'A': 4, 'F': 4}

    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = 'B'
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

    print(visited)




###############################################################################

# return maximum number of balls that can be collected
def max_balls(A, B):
    vertices = set(A)
    for b in set(B):
        vertices.add(b)
    V = len(vertices)
    #print(vertices)
    g = GraphAdjMatrix(V, vertices)
    for i in range(len(A)-1):
        g.add_edge(A[i], A[i+1])
        g.add_edge(B[i], B[i+1])
        if A[i] == B[i]:
            g.add_edge(A[i], B[i])
    print(g)

    graph_dfs(g)

    
    return -1

###############################################################################

if __name__ == "__main__":

    """
    #     0  1  2  3  4
    #   +---------------
    # 0 | 0  1  0  0  1
    # 1 | 1  0  1  1  1
    # 2 | 0  1  0  1  0
    # 3 | 0  1  1  0  1
    # 4 | 1  1  0  1  0
    V = 5
    g = GraphAdjMatrix(V, [0,1,2,3,4])
    g.add_edges([(0,4),(0,1),(4,1),(4,3),(3,1),(3,2),(1,2)])
    print(g)

    graph = GraphAdjList(V) 
    graph.add_edges([(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)])
    graph.print_graph() 
   
    sys.exit()
    """

    test_inputs = []
    test_inputs.append( (5, 5, "1 4 5 6 8", "2 3 4 6 9", 29) )

    """ Run process on sample inputs 
    """
    for N, M, inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        print(f'N={N} M={M}   {inputs1}   {inputs2}')
        rv = max_balls(arr1, arr2)
        print(f"{rv} expected: {results}")


    #dijkstras_shortest_path()

