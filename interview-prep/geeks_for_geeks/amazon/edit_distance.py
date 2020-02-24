import sys


# Given two strings str1 and str2 and below operations that can performed on str1.
# Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
#
# Insert
# Remove
# Replace
#
# All of the above operations are of equal cost.

def get_edit_distance(str1, str2):
    return edit_distance(str1, str2, len(str1), len(str2))

def edit_distance(str1, str2, m, n):
    if m == 0:  # if first string is empty, insert all elements of the second string (n inserts)
        return n

    if n == 0:  # if second string is empty, insert all elements of the first string (m inserts)
        return m

    if str1[m-1] == str2[n-1]:  # if last chars are equal, find edit distance ignoring these last chars
        return edit_distance(str1, str2, m-1, n-1)

    insert_cost = edit_distance(str1, str2, m, n-1)
    remove_cost = edit_distance(str1, str2, m-1, n)
    replace_cost = edit_distance(str1, str2, m-1, n-1)
    return 1 + min(insert_cost, remove_cost, replace_cost)

if __name__ == "__main__":

    print(get_edit_distance("geek", "gesek"))       # 1
    print(get_edit_distance("cat", "cut"))          # 1
    print(get_edit_distance("sunday", "saturday"))  # 3
    