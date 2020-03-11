import sys

# http://www.interviewcake.com/question/python/stock-price

# find best profit that could have been made with ONE purchase and ONE sale of stock

def max_profit(arr):
    print(arr)
    N = len(arr)
    first, last = arr[0], arr[N-1]
    i1, i2 = 0, N-1
    maxp = 0
    for i in range(N):
        p1 = last - arr[i]
        p2 = arr[N-i-1] - first
        if p1+p2 > maxp:
            maxp = p1 + p2
            i1 = i
            i2 = N-i-1
        #print(i1, ',', i2, ':', p1, p2, '   ', p1+p2)
    return f"{arr[i2]-arr[i1]}  A[{i1}] A[{i2}]  "

# This is the given ("correct") answer:
# complexity O(n) time and O(1) space
def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError("Getting a profit requires at least 2 prices")

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)
    return max_profit

if __name__ == "__main__":

    stock_prices_list = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 7, 2, 1, 8, 3, 5, 7],
        [1, 5, 4, 3, 8, 2, 20],
        [2, 5, 4, 3, 8, 1, 20],
        [10, 7, 5, 8, 11, 9]
    ]

    for stock_prices in stock_prices_list:
        print(max_profit(stock_prices), get_max_profit(stock_prices))
