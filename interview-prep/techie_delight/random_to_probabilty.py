import sys
import random

# https://www.techiedelight.com/get-0-1-equal-probability-using-specified-function/
# https://www.techiedelight.com/generate-0-1-75-25-probability/
# https://www.techiedelight.com/generate-fair-results-biased-coin/

def biased_coin():
    return 0 if random.randint(1,10) > 7 else 1

def fair_results_biased_coin():
    coin1 = coin2 = 0
    while coin1 == coin2:
        coin1 = biased_coin()
        coin2 = biased_coin()
    return coin1

def random01():
    return random.randint(0,1)

def random5():
    return random.randint(1,5)

# use above random function to return 0 or 1 with equal probability
def zero_one_50_50():
    rnd = 5
    while rnd == 5:
        rnd = random5()
    return rnd % 2

# use above 50/50 random function to return 0 or 1 with probabilities of 75 and 25
def zero_one_75_25():
    rnd = random01() + random01() ^ 2   # 0 to 3
    return 1 if rnd == 0 else 0

def check_probabilities(func, iter_count = 100000):
    total = 0
    for i in range(iter_count):
        rv = func()
        total += rv
    p = total / iter_count
    print((1-p) * 100)
    print(p * 100)
    print()

###############################################################################
if __name__ == "__main__":

    check_probabilities(zero_one_50_50)
    check_probabilities(zero_one_75_25)
    check_probabilities(biased_coin)
    check_probabilities(fair_results_biased_coin)
