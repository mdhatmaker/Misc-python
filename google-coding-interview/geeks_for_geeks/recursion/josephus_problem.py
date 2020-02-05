import sys

# https://practice.geeksforgeeks.org/problems/josephus-problem/1

# Given the total number of persons n and a number k which indicates that
# k-1 persons are skipped and kth person is killed in circle in a fixed direction.​
# The task is to choose the safe place in the circle so that when you perform these
# operations starting from 1st place in the circle, you are the last one remaining
# and survive.

###############################################################################

def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k-1) % n + 1

# n = number of people; k = kth person is killed (k-1 people skipped)
def josephus_problem(n, k):
    return josephus(n, k)


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("3 2", 3) )
    test_inputs.append( ("5 2", 3) )
    test_inputs.append( ("5 3", 4) )
    test_inputs.append( ("7 3", 4) )
    test_inputs.append( ("14 2", 13) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        rv = josephus_problem(arr[0], arr[1])
        print(f"{rv} expected: {results}")

