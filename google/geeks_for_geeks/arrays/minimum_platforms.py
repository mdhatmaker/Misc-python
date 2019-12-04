import sys

# https://practice.geeksforgeeks.org/problems/minimum-platforms/0

# Given arrival and departure times of all trains that reach a railway station.
# Your task is to find the minimum number of platforms required for the railway
# station so that no train waits.
#
# Note: Consider that all the trains arrive on the same day and leave on the same day.
# Also, arrival and departure times will not be same for a train, but we can have
# arrival time of one train equal to departure of the other.
#
# In such cases, we need different platforms, i.e at any given instance of time,
# same platform can not be used for both departure of a train and arrival of another.

def platforms_needed(arrive, depart):
    max_platforms = 0
    ia = 0
    id = 0
    platforms = []
    while ia < len(arrive) or id < len(depart):
        #print(platforms)
        max_platforms = max(len(platforms), max_platforms)
        if ia >= len(arrive):
            #print("depart:", id, depart[id])
            platforms.remove(id)
            id += 1
        elif id >= len(depart):
            #print("arrive:", ia, arrive[ia])
            platforms.append(ia)
            ia += 1
        elif arrive[ia] <= depart[id]:
            #print("arrive:", ia, arrive[ia])
            platforms.append(ia)
            ia += 1
        else:
            #print("depart:", id, depart[id])
            platforms.remove(id)
            id += 1

    return max_platforms


if __name__ == "__main__":

    # Note: Time intervals are in the 24-hour format(hhmm), of the form HHMM ,
    # where the first two charcters represent hour (between 00 to 23 ) and 
    # last two characters represent minutes (between 00 to 59).
    # input tuple: ("one arrival time for each train", "one departure time for each train", correct_result)
    test_inputs = []
    test_inputs.append( ("0900 0940 0950 1100 1500 1800", "0910 1200 1120 1130 1900 2000", 3) )
    test_inputs.append( ("0900 1100 1235", "1000 1200 1240", 1) )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arrive = [int(s) for s in inputs1.split()]
        depart = [int(s) for s in inputs2.split()]
        print(arrive, '\n', depart)
        count = platforms_needed(arrive, depart)
        print(f"{count} expected: {results}\n")

