import win32gui
import time

w=win32gui

while True:
    fgWindow = w.GetForegroundWindow()
    print fgWindow, w.GetWindowText(fgWindow)
    #r = raw_input("");
    time.sleep(1)

print "done."
