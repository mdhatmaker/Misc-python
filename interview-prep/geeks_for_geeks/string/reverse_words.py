import sys

# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0


# Given a String of length S, reverse the whole string without reversing the
# individual words in it. Words are separated by dots.



def reverse_words(s):
    split = my_split(s, '.')
    my_reverse(split)
    rev = '.'.join(split)
    return rev

def my_reverse(arr):
    i1 = 0
    i2 = len(arr)-1
    while i1 < i2:
        arr[i1], arr[i2] = arr[i2], arr[i1]
        i1 += 1
        i2 -= 1
    return

# Function to split string at given separator and return array of words
# O(n) to loop through entire string
def my_split(s, sep):
    arr = []
    i1 = i2 = 0
    while i2 <= len(s):
        if i2 >= len(s) or s[i2] == sep:
            arr.append(s[i1:i2])
            i2 += 1
            i1 = i2
        else:
            i2 += 1
    return arr

# Function to split string at given separator and return array of words in reverse order
# O(n) to loop through entire string (in reverse) looking for separator chars
def my_reverse_split(s, sep):
    arr = []
    i1 = len(s)-1
    i2 = len(s)
    while i1 >= -1:
        if i1 < 0 or s[i1] == sep:
            word = s[i1+1:i2]
            arr.append(word)
            i2 = i1
        i1 -= 1
    return arr



if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("i.like.this.program.very.much", "much.very.program.this.like.i") )
    test_inputs.append( ("pqr.mno", "mno.pqr") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(arr)
        rev = reverse_words(inputs)
        print(f"{rev} expected: {results}\n")

