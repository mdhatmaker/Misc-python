from os import listdir, curdir
from os.path import isdir, isfile, join

file_count = 0
line_count = 0

def file_len(fname):
    i = -1
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def list_files(path, ext='.py'):
    global file_count, line_count
    #print "LISTING FILES FOR PATH:", path
    for f in listdir(path):
        pathname = join(path, f)
        if isdir(pathname):
            list_files(pathname, ext)
        elif isfile(pathname) and f[-3:] == ext:
            print f
            file_count += 1
            line_count += file_len(pathname)
        #if os.isdir(f)

########################################################################################################################
#if __name__ == "__main__":

#path = r"X:\Users\Trader\Dropbox\dev\PROJECTS\python-projects"
#path = r"X:\Users\Trader\Dropbox\dev\python"
path = r"X:\Users\Trader\Dropbox\dev\csharp\PythonUI"
ext = '.cs'
list_files(path, ext)

print
print curdir
print path
print "\nFILE COUNT:", file_count
print "LINE COUNT:", line_count

