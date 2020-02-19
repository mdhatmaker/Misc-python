import sys

# https://practice.geeksforgeeks.org/problems/parenthesis-checker/0


# Given an expression string exp. Examine whether the pairs and the orders
# of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
# For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}”
# and 'not balanced' for exp = “[(])”

###############################################################################

stack = []

def push(x):
    stack.append(x)
    return

def pop():
    return stack.pop()

def is_balanced(s):
    for ch in s:
        if ch == '{' or ch == '(' or ch == '[':
            push(ch)
        else: #if ch == '}' or ch == ')' or ch == ']'
            from_stack = pop()
            if ch == '}' and from_stack != '{': return False
            if ch == ')' and from_stack != '(': return False
            if ch == ']' and from_stack != '[': return False
    return len(stack) == 0

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("{([])}", True) )
    test_inputs.append( ("()", True) )
    test_inputs.append( ("([]", False) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        print(f'{inputs}')
        tf = is_balanced(inputs)
        print(f"{tf} expected: {results}\n")

