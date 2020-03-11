import sys


if __name__ == "__main__":

    # Google interview question: given a string, return the first recurring
    # character in the string (or None if no recurring char exists)

    def first_recur(s):
        bag = {}
        N = len(s)
        for i in range(int(N / 2)):
            if s[i] in bag: return s[i]
            bag[s[i]] = True
            if s[N-i-1] in bag: return s[N-i-1]
            bag[s[N-i-1]] = True
        return None

    print(first_recur('ABCA'))
    print(first_recur('BCABA'))
    print(first_recur('ABBC'))
    print(first_recur('ABC'))

    sys.exit()

    # Facebook interview question: mapping letters of alphabet to 1-to-26,
    # decode all possible forms of message like '121' (i.e. 1-2-1, 12-1, 1-21 but
    # converted to their alpha equivalents)

    # 'a'->'1', 'b'->'2', ... 'z'->'26'
    mapping = {}
    for i in range(26):
        ch = chr(ord('a') + i)
        mapping[str(i+1)] = ch

    # firstdigit dictionary contains all mapping destinations that start with given digit
    firstdigit = {}
    for char, digits in mapping.items():
        if digits[0] in firstdigit:
            firstdigit[digits[0]].append(digits)
        else:
            firstdigit[digits[0]] = [digits]

    #print(mapping)
    #print(firstdigit)

    def get_msg(code):
        #print('code:', code)
        if not code: return '' #','
        for digits, ch in mapping.items():
            if code.startswith(digits):
                #print('ch:', ch)
                #print(ch + get_msg(code[len(ch):]), end='')
                print(ch, end='')
                print(get_msg(code[len(ch):]), end='')
        return '\n' #'|\n'

    #get_msg('123')



    # Amazon interview question: Recursive Staircase Problem
    # (can either take 1 or 2 steps)
    def num_ways(N, current = 0):
        if current > N:
            return 0
        elif current == N:
            return 1
        else:
            return num_ways(N, current+1) + num_ways(N, current+2)

    possible_steps = [1, 3, 5]
    def num_waysB(N, current = 0):
        if current > N:
            return 0
        elif current == N:
            return 1
        else:
            acc = 0
            for steps in possible_steps:
                acc += num_waysB(N, current + steps)
            return acc

    print(num_ways(4))
    print(num_ways(2))
    print(num_ways(3))

    print(num_waysB(3))


