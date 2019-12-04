import sys
import heapq

# https://practice.geeksforgeeks.org/problems/huffman-decoding-1/1
# https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

# Given an encoded string, your task is to print the decoded String.

###############################################################################

def decode(arr):
    
    return -1

def decode_file(root, s):   # struct MinHeapNode* root, string s)
    ans = ""
    curr = root     # struct MinHeapNode* curr = root;
    for i in range(len(s)):
        if s[i] == '0': curr = curr.left
        else:
            curr = curr.right

        if (not curr.left) and (not curr.right):
            ans += curr.data
            curr = root
    return ans + '\0'

"""   
Steps to build Huffman Tree
Input is an array of unique characters along with their frequency
of occurrences and output is Huffman Tree.

1. Create a leaf node for each unique character and build a min
heap of all leaf nodes. (Min Heap is used as a priority queue.
The value of frequency field is used to compare two nodes in min
heap. Initially, the least frequent character is at root)

2. Extract two nodes with the minimum frequency from the min heap.

3. Create a new internal node with a frequency equal to the sum of
the two nodes frequencies. Make the first extracted node as its
left child and the other extracted node as its right child. Add
this node to the min heap.

4. Repeat steps #2 and #3 until the heap contains only one node.
The remaining node is the root node and the tree is complete.
"""

class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.data}:{self.freq}'

    def __lt__(self, other):
        if other and self.freq < other.freq: return True
        else:
            return False

    def __gt__(self, other):
        if other and self.freq > other.freq: return True
        else:
            return False

    def __eq__(self, other):
        if other and self.freq == other.freq: return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


def build_huffman_tree(arr):
    minHeap = []
    for i in range(0, len(arr), 2):
        item = (int(arr[i+1]), arr[i])
        heapq.heappush(minHeap, item)
    #while minHeap:
    #    print(heapq.heappop(minHeap), end=' ')
    #print()
    
    #struct MinHeapNode *left, *right, *top; 
  
    # Step 1: Create a min heap of capacity equal to size.  Initially, there are 
    # nodes equal to size. 
    #struct MinHeap* minHeap = createAndBuildMinHeap(data, freq, size); 
  
    # Iterate while size of heap doesn't become 1 
    while not len(minHeap) == 1:    # isSizeOne(minHeap):
        # Step 2: Extract the two minimum freq items from in heap
        left = heapq.heappop(minHeap)   # extractMin(minHeap); 
        right = heapq.heappop(minHeap)  # extractMin(minHeap); 
  
        # Step 3:  Create a new internal node with frequency equal to the sum of the
        # two nodes frequencies. Make the two extracted node as left and right children
        # of this new node. Add this node to the min heap.
        # '$' is a special value for internal nodes, not used
        item = (left[0]+right[0], '$')  # (left.freq + right.freq, '$')
        heapq.heappush(minHeap, item)

        #top = newNode('$', left->freq + right->freq); 
        #top->left = left; 
        #top->right = right; 
        #insertMinHeap(minHeap, top); 
    
    # Step 4: The remaining node is the root node and the tree is complete. 
    return heapq.heappop(minHeap)   # extractMin(minHeap); 



###############################################################################

if __name__ == "__main__":

    test_inputs = []
    #test_inputs.append( ("abc", "abc") )
    #test_inputs.append( ("geeksforgeeks", "geeksforgeeks") )
    test_inputs.append( ("a 5 b 9 c 12 d 13 e 16 f 45", "") )


    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [s for s in inputs.split()]
        print(f'{inputs}')
        rv = build_huffman_tree(arr)
        print(f"{rv} expected: {results}")

    #minHeap = rv
    #while minHeap:
    #    print(heapq.heappop(minHeap), end=' ')
    #print()
