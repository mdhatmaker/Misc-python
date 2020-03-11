import sys

# https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1

# Given a weighted, undirected and connected graph. The task is to find the sum
# of weights of the edges of the Minimum Spanning Tree.

###############################################################################

class Node:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __repr__(self):
        return f'{self.vertex1} {self.vertex2} {self.weight}'

# return sum of weights of the edges of the Minimum Spanning Tree
def spanning_tree(arr, nedges):
    for i in range(0, len(arr), 3):
        n = Node(arr[i], arr[i+1], arr[i+2])
        print('node:', n)

    return -1

###############################################################################

if __name__ == "__main__":

    # E denotes the number of nodes and number of edges.
    # Then inputs has 3*E space-separated values a b w where a, b denotes an edge
    # from a to b and w is the weight of the edge.
    test_inputs = []
    test_inputs.append( (3, "1 2 5 2 3 3 1 3 1", 4) )
    test_inputs.append( (1, "1 2 5", 5) )

    """ Run process on sample inputs 
    """
    for E, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{inputs}')
        rv = spanning_tree(arr, E)
        print(f"{rv} expected: {results}")
