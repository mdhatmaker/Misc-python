import sys

# https://practice.geeksforgeeks.org/problems/geek-collects-the-balls/0
# https://www.geeksforgeeks.org/graph-and-its-representations/
# https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php

# There are two parallel roads, each containing N and M buckets, respectively. Each
# bucket may contain some balls. The buckets on both roads are kept in such a way that
# they are sorted according to the number of balls in them. Geek starts from the end
# of the road which has the bucket with a lower number of balls (i.e. if buckets are
# sorted in increasing order, then geek will start from the left side of the road).
# The geek can change the road only at the point of intersection (which means, buckets
# with the same number of balls on two roads). Now you need to help Geek to collect
# the maximum number of balls.

###############################################################################

import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize #sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def __lt__(self, other):
        return (other and self.id < other.id)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def add_vertex_list(self, node_list):
        for n in node_list:
            self.add_vertex(n)

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def add_edges(self, edge_list):
        for e in edge_list:
            src,dest,cost = e
            self.add_edge(src, dest, cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print('''Dijkstra's shortest path''')
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

# code that demonstrates the use of the dijkstra algorithm
def test_dijkstra():
    g = Graph()
    g.add_vertex_list(['a','b','c','d','e','f'])
    g.add_edges([('a','b',7),('a','c',9),('a','f',14),('b','c',10),('b','d',15),('c','d',11),('c','f',2),('d','e',6),('e','f',9)])  
    print('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
    dijkstra(g, g.get_vertex('a'), g.get_vertex('e')) 
    target = g.get_vertex('e')
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : %s' %(path[::-1]))


###############################################################################

# return maximum number of balls that can be collected
def max_balls(A, B):
    vertices = set(A).union(set(B))
    V = len(vertices)
    #print(vertices)
    #g = GraphAdjMatrix(V, vertices)
    g = Graph()
    #g.add_vertex_list(['a','b','c','d','e','f'])
    g.add_vertex_list(list(vertices))
    #g.add_edges([('a','b',7),('a','c',9),('a','f',14),('b','c',10),('b','d',15),('c','d',11),('c','f',2),('d','e',6),('e','f',9)])  
 
    for i in range(len(A)-1):
        g.add_edge(A[i], A[i+1], A[i])
        g.add_edge(B[i], B[i+1], B[i])
        if A[i] == B[i]:
            g.add_edge(A[i], B[i], A[i])
    for v in g: print(v)
    #print(g)
    
    return -1


###############################################################################

if __name__ == "__main__":

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



