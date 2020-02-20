import sys
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

### https://youtu.be/Ercd-lp5PfQ

# Run 'live_data_gen.py' concurrently to add to the data file

plt.style.use('fivethirtyeight')

#x_vals = [0, 1, 2, 3, 4, 5]
#y_vals = [0, 1, 3, 2, 3, 5]
#plt.plot(x_vals, y_vals)
x_vals = []
y_vals = []

index = count()     # count function counts up each time it is called

def animate(i):
    #x_vals.append(next(index))
    #y_vals.append(random.randint(0,5))
    data = pd.read_csv('live_data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()       # clear axis
    # note: there is a (more complicated way) to update without clearing the axis

    #plt.plot(x_vals, y_vals)
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')    # because the cla function also clears the legend
    plt.tight_layout()

# FuncAnimation also has an initfunc argument to perform initialization
# FuncAnimation aslo has fargs argument to pass in other arguments

ani = FuncAnimation(plt.gcf(), animate, interval=1000)  # gcf = Get Current Figure

plt.tight_layout()
plt.show()



