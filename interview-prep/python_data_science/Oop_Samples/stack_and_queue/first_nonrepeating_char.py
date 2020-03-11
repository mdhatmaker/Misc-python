import sys
from StackAndQueue import Stack, Queue

# https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/0


# Given an input stream of N characters consisting only of lower case alphabets.
# The task is to find the first non repeating character, each time a character is
# inserted to the stream. If no non repeating element is found print -1.

###############################################################################


s1 = Stack()
s2 = Stack()

q = Queue()


def find_nonrepeating_chars(arr):
    s1.clear()
    s2.clear()
    q.clear()
    values = []
    i = 0
    while i < len(arr):
        values.append(arr[i])
        
        i += 1
    return values

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("a a b c", "a -1 b b") )
    test_inputs.append( ("a a c", "a -1 c") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [s for s in inputs.split()]
        print(f'{arr}')
        rv = find_nonrepeating_chars(arr)
        print(f"{rv} expected: {results}\n")

