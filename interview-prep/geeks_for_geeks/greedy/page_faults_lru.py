import sys

# https://practice.geeksforgeeks.org/problems/page-faults-in-lru/0


# In operating systems that use paging for memory management, page replacement algorithm
# are needed to decide which page needs to be replaced when the new page comes in.
# Whenever a new page is referred and is not present in memory, the page fault occurs
# and Operating System replaces one of the existing pages with a newly needed page.
# Given a sequence of pages and memory capacity, your task is to find the number of
# page faults using Least Recently Used (LRU) Algorithm.

###############################################################################

INT_MAX = 999999999

def count_page_faults(pages, capacity):
    in_memory = {}
    indexes = {}
    page_faults = 0
    for i, pg in enumerate(pages):
        # Check if the set can hold more pages
        if len(in_memory) < capacity:
            # Insert it into set if not present already (page fault)
            if not pg in in_memory:
                in_memory[pg] = True
                page_faults += 1                # increment page faults
        else:   
            # If the set is full then need to perform LRU i.e. remove the least recently
            # recently used page and insert the current page

            # Check if current page is not already present in the set (page fault)
            if not pg in in_memory:
                # Find the least recently used page that is present in the set 
                lru = INT_MAX
                val = 0
                for it in in_memory: 
                    if indexes[it] < lru:
                        lru = indexes[it]; 
                        val = it; 

                del in_memory[val]              # remove the indexes page 
                in_memory[pg] = True            # insert the current page 
                page_faults += 1                # increment page faults 

        indexes[pg] = i             # store/update the recently-used index of the page
        #print(in_memory, indexes)
    return page_faults

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (4, "5 0 1 3 2 4 1 0 5", 8) )
    test_inputs.append( (4, "3 1 0 2 5 4 1 2", 7) )
    test_inputs.append( (4, "7 0 1 2 0 3 0 4 2 3 0 3 2", 6) )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{k} {arr}')
        rv = count_page_faults(arr, k)
        print(f"{rv} expected: {results}")


