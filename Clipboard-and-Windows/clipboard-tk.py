from Tkinter import Tk
import sys

r = Tk()
r.withdraw()


data = r.clipboard_get()
#print(data)
data = data.split('\n')

li = [d[1:-1] for d in data]

for i in range(len(li)):
    ix = li[i].rfind('\\') + 1
    li[i] = li[i][ix:]

li.sort()

r.clipboard_clear()

for i in range(len(li)):
    print(li[i])
    r.clipboard_append(li[i] + '\n')


r.update() # now it stays on the clipboard after the window is closed
r.destroy()



