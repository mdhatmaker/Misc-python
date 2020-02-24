import sys


# return nth ugly number (number whose only prime factors are 2, 3, 5 -- 1 is ugly by default)
# first 11 ugly numbers: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
def ugly_number(n):
    ugly = [0] * n
    ugly[0] = 1 # 1 is ugly number by default
    for i in range(1, n-3, 3):
        ugly[i] = 2 * ugly[i-1]
        ugly[i+1] = 3 * ugly[i-1]
        ugly[i+2] = 5 * ugly[i-1]
        print(ugly[i], ugly[i+1], ugly[i+2])


if __name__ == "__main__":

    print(ugly_number(11))
