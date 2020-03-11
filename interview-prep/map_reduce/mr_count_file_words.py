import multiprocessing
import string

from multiprocessing_mapreduce import SimpleMapReduce

# https://pymotw.com/2/multiprocessing/mapreduce.html

# The Pool class can be used to create a simple single-server MapReduce implementation.
# Although it does not give the full benefits of distributed processing, it does
# illustrate how easy it is to break some problems down into distributable units of work.

# In a MapReduce-based system, input data is broken down into chunks for processing
# by different worker instances. Each chunk of input data is mapped to an intermediate
# state using a simple transformation. The intermediate data is then collected together
# and partitioned based on a key value so that all of the related values are together.
# Finally, the partitioned data is reduced to a result set.


def file_to_words(filename):
    """Read a file and return a sequence of (word, occurances) values.
    """
    STOP_WORDS = set([
            'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in', 
            'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the', 'to', 'with',
            ])
    #TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    # The string.maketrans() function is deprecated and is replaced by new static methods,
    # bytes.maketrans() and bytearray.maketrans(). This change solves the confusion around
    # which types were supported by the string module. Now, str, bytes, and bytearray
    # each have their own maketrans and translate methods with intermediate translation
    # tables of the appropriate type.
    TR = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

    print(multiprocessing.current_process().name, 'reading', filename)
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            if line.lstrip().startswith('..'): # Skip rst comment lines
                continue
            line = line.translate(TR) # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append( (word, 1) )
    return output


def count_words(item):
    """Convert the partitioned data for a word to a
    tuple containing the word and the number of occurances.
    """
    word, occurances = item
    return (word, sum(occurances))


if __name__ == '__main__':
    import operator
    import glob

    #input_files = glob.glob('*.rst')
    input_files = glob.glob('*.py')

    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()
    
    print('\nTOP 20 WORDS BY FREQUENCY\n')
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print('%-*s: %5s' % (longest+1, word, count))