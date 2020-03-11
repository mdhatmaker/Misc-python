import sys

#https://www.techiedelight.com/find-number-even-odd-without-using-conditional-statement/

# Find if a number is even or odd without using any conditional statement

if __name__ == "__main__":

    n = 31

    # using short-circuit boolean logic
    #((n & 1) and print("odd")) or print("even")
    print("odd") if (n & 1) else print("even")

    # using string
    eo = ['even', 'odd']
    print(eo[n % 2])
    print(eo[n & 1])

    # using while loop (C++ only)
    #while (num-- > 0 && --num > 0) { }
    # if num is 0, number is even
    # if num is 1, number is odd

