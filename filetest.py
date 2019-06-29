try:
    f = open(r'/somefile.txt')
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
    

    
