import sys

# https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places/0


# Given two strings a and b. The task is to find if a string 'a' can be obtained by
# rotating another string 'b' by 2 places.

# Given a number of places to rotate, check the rotated string for each rotate position.
# i.e. if places == 2, check rotate of -2, -1, 0, 1, 2
def check_rotate_places(s1, s2, places):
    for rotate in range(-places, places+1):
        if equal_with_rotate(s1, s2, rotate):
            return 1
    return 0
 
def get_char(s, index):
    i = index % len(s)
    return s[i]

# Function to determine if two strings are equal if the 2nd string is rotated by the given amount.
def equal_with_rotate(s1, s2, rotate):
    if len(s1) != len(s2): return False
    if rotate == 0: return s1 == s2
    for i1 in range(len(s1)):
        if get_char(s1, i1) != get_char(s2, rotate + i1):
            return False
    return True

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("amazon", "azonam", 1) )
    test_inputs.append( ("geeksforgeeks", "geeksgeeksfor", 0) )

    """ Run process on sample inputs 
    """
    for s1, s2, results in test_inputs:
        print (s1, s2)
        rotate_places = 2
        tf = check_rotate_places(s1, s2, rotate_places)
        print(f"{tf} expected: {results}\n")

