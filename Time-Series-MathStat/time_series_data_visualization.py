# Note: The downloaded file contains some question mark (“?”) characters that must be removed
# before you can use the dataset. Open the file in a text editor and remove the “?” characters.
# Also remove any footer information in the file.

from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from matplotlib import pyplot
import sys


def test1():
    series = Series.from_csv('daily-minimum-temperatures.csv', header=None)
    print(series.head())
    return


def test2():
    series = Series.from_csv('daily-minimum-temperatures.csv', header=0) #, error_bad_lines=False)
    series.plot()
    pyplot.show()
    return

def test3():
    groups = series.groupby(TimeGrouper('A'))
    years = DataFrame()
    for name, group in groups:
        years[name.year] = group.values
    years.plot(subplots=True, legend=False)
    pyplot.show()
    return

################################################################################


series = Series.from_csv('daily-minimum-temperatures.csv', header=None) #, error_bad_lines=False) #, na_values="")
print(series)
series.astype('float')

#pyplot.plot(series) #, 'k.')
#pyplot.show()

#-------------------------------------------------------------------------------
"""
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
groups = series.groupby(TimeGrouper('A'))
years = DataFrame()

#for n,g in groups:
#    print(n,g)

#for name, group in groups:
#    print(name, name.year, group.values)
#    #years[name.year] = group.values

for name, group in groups:
    print(name.year, group.values)
    #years[name] = group.values

pyplot.plot(years, subplots=True, legend=False)
pyplot.show()
"""
#-------------------------------------------------------------------------------
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)

groups = series.groupby(TimeGrouper('A'))
years = DataFrame()
years = {}



#for n,g in groups:
#    print(n,g)

#for name, group in groups:
#    print(name, name.year, group.values)
#    #years[name.year] = group.values

for name, group in groups:
    #print(name.year, group.values)
    years[name.year] = group.values

for y in years:
    print(y)
    pyplot.plot(y)

sys.exit()

pyplot.plot(years, subplots=True, legend=False)
pyplot.show()



