import sys
import os
from os import listdir
from os.path import isfile, join
import pandas as pd

#-----------------------------------------------------------------------------------------------------------------------

execfile("f_folders.py")
execfile("f_date.py")
raw_folder = join(folder, "RAW_DATA")
df_folder = join(folder, "DF_DATA")

#-----------------------------------------------------------------------------------------------------------------------


def convert_multichart_file(input_filename):
    (pathname, extension) = os.path.splitext(input_filename)
    #(drive, path) = os.path.splitdrive(line)
    (path, filename)  = os.path.split(pathname)

    input_pathname = join(raw_folder, input_filename)
    dataframe_pathname = join(df_folder, filename + ".csv")

    print "Converting multichart data file:", "'" + filename + ".txt'"

    fin = open(input_pathname, 'r')
    fout = open(dataframe_pathname, 'w')
    line = fin.readline().strip()
    if line != "<Date>, <Time>, <Open>, <High>, <Low>, <Close>, <Volume>":
        raise Exception("First line of Multichart file should be '<Date>, <Time>, <Open>, <High>, <Low>, <Close>, <Volume>'")
    fout.write("DateTime,Open,High,Low,Close,Volume\n")

    line = fin.readline().strip()
    while line:
        #print line
        columns = line.split(',')
        # Each line contains Date,Time,Open,High,Low,Close,Volume
        d = columns[0]
        t = columns[1]
        o = columns[2]
        h = columns[3]
        l = columns[4]
        c = columns[5]
        v = columns[6]
        dt = get_datetime(d, t)
        fout.write("{0},{1},{2},{3},{4},{5}\n".format(dt, o, h, l, c, v))
        line = fin.readline().strip()
    fin.close()
    fout.close()
    return

################################################################################

print "Multichart data export to pandas dataframe"
print "Input Folder:", raw_folder
print "Output Folder:", df_folder
print

#multichart_filename = "GASF16-GASG16 1 Hour.txt"
multichart_filename = ""

if multichart_filename == "":
    txt_files = [ f for f in listdir(raw_folder) if (isfile(join(raw_folder, f)) and f.endswith('.txt')) ]
    for f in txt_files:
        convert_multichart_file(f)
else:
    convert_multichart_file(multichart_filename)

print
print "Done."

