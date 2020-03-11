import sys


# Function to reverse a string (in-place)
# (In Python, strings are immutable, so you can't change their characters in-place.)
def reverse(s):
    i1 = 0
    i2 = len(s)-1
    li = list(s)
    print(li)
    while i1 < i2:
        temp = li[i1]
        li[i1] = li[i2]
        li[i2] = temp
        i1 += 1
        i2 -= 1
    print(li)
    return ''.join(li)


if __name__ == "__main__":

    print(reverse("Michael"))
    
    