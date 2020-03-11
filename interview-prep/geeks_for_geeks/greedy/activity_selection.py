import sys

# https://practice.geeksforgeeks.org/problems/activity-selection/0
# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0
# http://www.cs.umd.edu/class/fall2017/cmsc451-0101/Lects/lect07-greedy-sched.pdf


# Given N activities with their start and finish times. Select the maximum number
# of activities that can be performed by a single person, assuming that a person
# can only work on a single activity at a time.
#
# Note : The start time and end time of two activities may coincide.

###############################################################################

class Times:
    def __init__(self, start_time, end_time):
        self.start = start_time
        self.end = end_time

    def __repr__(self):
        return f'({self.start}-{self.end})'

    """def conflicts_with(self, times):
        return not (times.start > self.end or times.end < self.start)"""


# Here, finally, is a greedy strategy that does work. Since we do not like activities
# that take a long time, let us select the activity that finishes first and schedule it.
# Then, we skip all activities that conflict with this one, and schedule the next one that
# has the earliest finish time, and so on. Call this strategy Earliest Finish First (EFF).
# The pseudo-code is presented in the code-block below. It returns the set S of scheduled activities.
# Greedy Interval Scheduling
"""greedyIntervalSchedule(s, f) {      // schedule tasks with given start/finish times
sort tasks by increasing order of finish times
S = empty
prev_finish = -infinit y
for (i = 1 to n) {
    if (s[i] > prev_finish) {
        append task i to S
        prev_finish = f[i]
    }
}
return S }"""


# Take list of start times and list of end times -- return list of Times objects
# that contain both start/end times.                                                                                                                          
def ArraysToTimes(arr1, arr2):
    li = []
    for i in range(len(arr1)):
        t = Times(arr1[i], arr2[i])
        li.append(t)
    return li

"""# initializing list of tuples 
test_list = [ ('a', 1), ('b', 2), ('c', 3), ('d', 4)]  
# initializing sort order  
sort_order = ['d', 'c', 'a', 'b'] 
# printing original list 
print ("The original list is : " + str(test_list))   
# printing sort order list 
print ("The sort order list is : " + str(sort_order)) 
# using sort() + lambda + index() 
# to sort according to other list  
test_list.sort(key = lambda(i, j): sort_order.index(i))"""

# Use this to sort the Times objects by end-time
def sortTimes(times):
    return times.end

def max_activities(arr1, arr2):
    unsorted_times = ArraysToTimes(arr1, arr2)
    times = sorted(unsorted_times, key=sortTimes)
    S = []
    prev_finish = -999999
    for i in range(0, len(times)):
        if times[i].start > prev_finish:
            S.append(times[i])
            prev_finish = times[i].end
            #print(times[i], end=' ')
    #print(S)
    return len(S)


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 3 2 5 8 5", "2 4 6 7 9 9", 4) )
    test_inputs.append( ("1 3 2 5", "1 3 2 5", 4) )
    test_inputs.append( ("1 3 0 5 8 5", "2 4 6 7 9 9", 4) )
    test_inputs.append( ("75250 50074 43659 8931 11273 27545 50879 77924", "112960 114515 81825 93424 54316 35533 73383 160252", 3) )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        print(f'{arr1} {arr2}')
        rv = max_activities(arr1, arr2)
        print(f"{rv} expected: {results}")


    """test_list = ['aaa', 'bbbbb', 'cccccccc', 'ddddddddddd', 'eeeeee']
    test_list.sort(key = lambda s: len(s))
    print(test_list)"""

