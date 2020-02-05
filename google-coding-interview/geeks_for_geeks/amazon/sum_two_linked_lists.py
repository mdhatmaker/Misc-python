import sys
from TreeAndList import LinkedList


# Given two numbers represented by two linked lists, write a function that
# returns the sum as another linked list

def sum_lists(ll1, ll2):
    rv = LinkedList()
    n1 = ll1.root
    n2 = ll2.root
    carry = 0
    while n1 or n2:
        if not n2:
            digit = n1.data
            n1 = n1.next
        elif not n1:
            digit = n2.data
            n2 = n2.next
        else:
            digit = n1.data + n2.data
            n1 = n1.next
            n2 = n2.next
        digit += carry
        carry = int(digit / 10)
        digit = digit % 10
        rv.append(digit)
    return rv

if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.append_list([5, 6, 3])  # represents number 365
    ll2 = LinkedList()
    ll2.append_list([8, 4, 2])  # represents number 248

    sum = sum_lists(ll1, ll2)   # output should be 3->1->6 (represents 613)
    sum.print_list()

