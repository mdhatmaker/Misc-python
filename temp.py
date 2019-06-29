folder = "/Users/michael/CLionProjects/TimeSeries/data/"


f = open(folder + "temp.csv", 'r')

line = f.readline()
while line:
    line = line[:-1]
    data = line.split(',')
    x = float(data[2])
    x = x * 100
    x = round(x, 2)
    data[2] = str(x)
    print ','.join(data)
    line = f.readline()

f.close()
