import sys


def map(k2, v2, mapped_list):
    item = (k2, v2)
    mapped_list.append(item)

def process(input, mapped_list):
    for ch in input:
        mlist = map(ch, 1, mapped_list)
     

if __name__ == "__main__":

    output = []
    output.append(('a', 1))
    output.append(('a', 1))
    output.append(('b', 1))
    word, occurances = output
    print(word, sum(occurances))
    sys.exit()

    all_inputs = ['XBB', 'CBA', 'XAC']

    #<k1, v1> -> Map() -> list(<k2, v2>)
    #<k2, list(v2)> -> Reduce() -> list(<k3, v3>)

    maps = []

    # split
    for input in all_inputs:
        # send each input to a different server (for parallel processing)

        # and on each server, run MAP to get results
        # {'X', 1}, {'B', 1}, {'B', 1}
        # {'C', 1}, {'B', 1}, {'A', 1}
        # {'X', 1}, {'A', 1}, {'C', 1}
        mapped_list = []
        process(input, mapped_list)
        maps.append(mapped_list)
        
    print(maps)

    # combine results 
    # {'A', 1}, {'A', 1}
    # {'B', 1}, {'B', 1}, {'B', 1}
    # {'C', 1}, {'C', 1}
    # {'X', 1}, {'X', 1}
    combined = {}
    for mlist in maps:
        for kv in mlist:
            mkey, mval = kv
            if mkey in combined:
                combined[mkey].append(kv)
            else:
                combined[mkey] = [kv]
    
    print(combined)

    # then reduce
    # {'A', 2}, {'B', 3}, {'C', 2}, {'X', 2}
    reduced = {}
    for kvkey, kvlist in combined.items():
        for k, v in kvlist:
            if kvkey in reduced:
                existing = reduced[k]
                reduced[k] += v
            else:
                reduced[k] = v

    print(reduced)



