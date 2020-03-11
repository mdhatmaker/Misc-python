import sys
import random

def random_input_from_given_probabilities():
    input = [1, 2, 3, 4, 5]
    prob = [30, 10, 20, 15, 25]     # probabilities should sum to 100

    sum = 0
    check = []
    for x in prob:
        sum += x
        check.append(sum)

    for xx in range(10):
        rnd = random.randint(1, 100)
        for i in range(len(check)-1):
            if rnd <= check[i]:
                print(rnd, input[i])
                break

    


if __name__ == "__main__":

    random_input_from_given_probabilities()

