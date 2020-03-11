import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
bar_width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# line plot is default of the plot method
#plt.plot(ages_x, dev_y, color="#444444", label="All Devs")
# bar plot
#plt.bar(ages_x, dev_y, color="#444444" ,label="All Devs")
# use numpy (as shown above) to have multiple bars
# shifted to the left
plt.bar(x_indexes - bar_width, dev_y, width=bar_width, color="#444444" ,label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
#plt.plot(ages_x, py_dev_y, color="#008fd5", label="Python")
plt.bar(x_indexes, py_dev_y, width=bar_width, color="#008fd5", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74383]
#plt.plot(ages_x, js_dev_y, color="#e5ae38", label="JavaScript")
# shifted to the right
plt.bar(x_indexes + bar_width, js_dev_y, width=bar_width, color="#e5ae38", label="JavaScript")


plt.legend()

# convert from integer indexes to age labels
plt.xticks(ticks=x_indexes, labels=ages_x)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD")

plt.tight_layout()

plt.show()
