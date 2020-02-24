import sys


# https://practice.geeksforgeeks.org/problems/longest-valid-parentheses/0

# Given a string S consisting of opening and closing parenthesis '(' and ')'.
# Find length of the longest valid parenthesis substring.

###############################################################################

def longest_valid_parens(s):
    stack = []
    count = max_count = 0
    for ch in s:
        if ch == '(':
            stack.append(ch)
            count = 0
        elif ch == ')':
            if len(stack) > 0:
                #p = stack.pop()
                count += stack.pop() + 2
                max_count = max(count, max_count)
            else:
                count = 0
                stack.clear()
        print(ch, stack, count, max_count)
    #max_count = max(count, max_count)
    return max_count

def solve(parenthesis):
    stack = []
    cur = 0
    ret = 0
    for e in parenthesis:
        if e == '(':
            stack.append(cur)
            cur = 0
        elif e == ')' and len(stack) > 0:
            cur += stack.pop() + 2
            ret = max(ret, cur)
        elif e == ')' and len(stack) == 0:
            cur = 0
    return ret

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("((()", 2) )
    test_inputs.append( (")()())", 4) )
    test_inputs.append( ("()(()", 2) )
    test_inputs.append( ("()(((()())", 6) )
    test_inputs.append( ("()()", 4) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{inputs}')
        rv = solve(inputs)
        print(f"{rv} expected: {results}")

