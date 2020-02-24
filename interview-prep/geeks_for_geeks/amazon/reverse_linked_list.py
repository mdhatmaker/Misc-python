import sys
from collections import deque
from TreeAndList import Node, BinaryTree, LinkedList


###############################################################################

if __name__ == "__main__":

    # LINKED LIST
    ll = LinkedList()
    ll.append_list([3, 4, 5, 6])
    ll.print_list()

    ll.reverse_inplace()
    ll.print_list()

    # BINARY TREE
    bt = BinaryTree()
    bt.add_list([5, 3, 1, 9, 7, 4])
    bt.print_tree()

    path1 = bt.find_path(3)
    path2 = bt.find_path(4)
    print(f'{path1}\n{path2}')

    print(bt.get_lca(4, 7))
    print(bt.get_lca(3, 4))

    print(bt.path_between(4, 7))

    print(bt.root.l, bt.root.r)   # .l and .r are properties identical to .prev and .next
