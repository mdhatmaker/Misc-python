import sys

# https://practice.geeksforgeeks.org/problems/roman-number-to-integer/0
# https://www.rapidtables.com/math/symbols/roman_numerals.html


# Given an string in roman no format (s)  your task is to convert it to integer .

roman_sort = { 'I': 1, 'V': 2, 'X': 3, 'L': 4, 'C': 5, 'D': 6, 'M': 7 }

roman = {}
roman['I'] = 1
roman['V'] = 5
roman['X'] = 10
roman['L'] = 50
roman['C'] = 100
roman['D'] = 500
roman['M'] = 1000

# TODO: I need to SUBTRACT if we have "backtracked" in Roman Numerals (i.e. 'I' comes before 'V')
def roman_to_integer(s):
    level = 0
    total = 0
    i1 = len(s)-1
    sort_level = -1
    while i1 >= 0:
        ch = s[i1]
        level = max(level, roman_sort[ch])
        if roman_sort[ch] < level:
            total -= roman[ch]
        else:
            total += roman[ch]
        i1 -= 1
    return total


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("I", 1) )
    test_inputs.append( ("V", 5) )
    test_inputs.append( ("III", 3) )
    test_inputs.append( ("IV", 4) )
    test_inputs.append( ("XII", 12) )
    test_inputs.append( ("MCMLXXXVIII", 1988) )
    test_inputs.append( ("MMXVI", 2016) )
    test_inputs.append( ("MMXVII", 2017) )
    test_inputs.append( ("MMXVIII", 2018) )
    test_inputs.append( ("MMXIX", 2019) )


    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        print(inputs)
        int_value = roman_to_integer(inputs)
        print(f"{int_value} expected: {results}\n")

