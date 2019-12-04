import sys

# https://practice.geeksforgeeks.org/problems/implement-strstr/1


# Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s.

# First occurence of x in s (-1 if not found)
def strstr(s, x):
    for i1 in range(len(s)-len(x)):
        if s[i1] == x[0]:
            same = True
            for i2 in range(len(x)):
                if s[i1+i2] != x[i2]:
                    same = False
                    break
            if same == True:
                return i1
        i1 += 1
    return -1


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("GeeksForGeeks", "Fr", -1) )
    test_inputs.append( ("GeeksForGeeks", "For", 5) )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        print(inputs1, inputs2)
        ix = strstr(inputs1, inputs2)
        print(f"{ix} expected: {results}\n")

