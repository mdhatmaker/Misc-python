import sys

"""typedef struct {
    item_type q[PQ_SIZE+1];     /* body of queue */
    int n;                      /* number of queue elements */
} priority_queue;"""

# For key at position [k]:
# left child at position [2k]
# right child at position [2k+1]
# parent of k at position [k/2]
#
# (assume array starts with index 1 to simplify matters)

class priority_queue:
    def __init__(self, pq_size=1000):
        self.pq_size = pq_size
        self.pq = [0] * (pq_size+1)         # body of priority queue
        self.nitems = 0                     # number of queue elements

    def pq_parent_index(self, n):
        if n == 1: return -1
        else:
            return int(n/2)     # implicitly take floor n/2

    def pq_left_child_index(self, n):
        return 2*n

    def pq_right_child_index(self, n):
        return 2*n + 1

    def get(self, n):
        return self.pq[n]

    def set(self, n, value):
        self.pq[n] = value

    def get_parent(self, n):
        if n == 1: return None
        else:
            return self.pq[int(n/2)]

    def set_parent(self, n, value):
        if n == 1: return
        else:
            self.pq[int(n/2)] = value

    def get_left_child(self, n):
        return self.pq[2*n]

    def set_left_child(self, n, value):
        self.pq[2*n] = value
        return 2*n

    def get_right_child(self, n):
        return self.pq[2*n+1]

    def set_right_child(self, n, value):
        self.pq[2*n+1] = value
        return 2*n+1


if __name__ == "__main__":

    pq = priority_queue(100)

    #                    1492
    #                 /        \
    #             1783          1776
    #            /    \        /    \
    #        1804     1865   1945   1963
    #       /   \     /   
    #    1918  2001  1941

    pq.set(1, 1492)
    lc0 = pq.set_left_child(1, 1783)
    rc0 = pq.set_right_child(1, 1776)
    lc = pq.set_left_child(lc0, 1804)
    rc = pq.set_right_child(lc0, 1865)
    pq.set_left_child(lc, 1918)
    pq.set_right_child(lc, 2001)
    pq.set_left_child(rc, 1941)
    pq.set_left_child(rc0, 1945)
    pq.set_right_child(rc0, 1963)

    print(pq.pq)

