import random


def print_board(arr):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            print(arr[r][c], end = ' ')
        print('')
    print('\n')
    return

def place_bombs(arr, max_bombs):
    for i in range(max_bombs):
        rr = random.randint(0, len(arr)-1)
        rc = random.randint(0, len(arr[0])-1)
        arr[rr][rc] = '*'
    return

def count_adj_bombs(arr, r, c):
    # [r-1] -> [c-1] [c] [c+1]
    # [r] -> [c-1] [c] [c+1]
    # [r+1] -> [c-1] [c] [c+1]
    if arr[r][c] == '*':
        return 0
    bomb_count = 0
    for ir in range(r-1, r+2):
        for ic in range(c-1, c+2):
            if ir >= 0 and ir < len(arr) and ic >= 0 and ic < len(arr[0]):
                if ir == r and ic == c:
                    continue
                if arr[ir][ic] == '*':
                    bomb_count += 1
    return bomb_count

def calculate_counts(arr):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            count = count_adj_bombs(arr, r, c)
            if count > 0:
                arr[r][c] = chr(ord('0') + count)
    return


if __name__ == '__main__':
    SIZE = 10

    #a = [['-'] * SIZE] * SIZE
    a = [['-'] * SIZE for i in range(SIZE)]

    print_board(a)

    place_bombs(a, 5)
    calculate_counts(a)

    #a[5][5] = '*'
    #print(a[5][5])

    print_board(a)