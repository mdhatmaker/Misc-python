import win32gui
import win32con
import win32api
import pywinauto
from pywinauto import Application
import time

print "Position cursor over technical indicator line and click left mouse button twice..."

while True:
    point = win32gui.GetCursorPos()
    #print point
    #cursor = win32gui.GetCursor()
    #print cursor & win32con.WM_LBUTTONDOWN, cursor & win32con.WM_LBUTTONUP
    state = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
    if state == -32767: break
    #print state
    
    time.sleep(.1)

print point

hwnd = win32gui.WindowFromPoint(point)
print hwnd
pt = win32gui.ScreenToClient(hwnd, point)
hw = pywinauto.controls.HwndWrapper.HwndWrapper(hwnd)

#print hw.MenuItems()

# connect to Excel
xlapp = Application()
xlapp.connect_(title_re = ".*Volume Bar*")

# create the XStudy application ousing a window handle
app = Application()
app.connect_(handle = hwnd)     # pass the window handle of one of the app's window

# right-click on the indicator
hw.Click(button='right', coords=pt)

# current value
#hw.TypeKeys('l~c', pause=0.5)
app.PopupMenu.MenuItem("Link To Excel->Current Value").Click()
xlapp.top_window_().TypeKeys("^v~")

valueCount = 22
for i in range(1, valueCount):
    # right-click on the indicator
    hw.Click(button='right', coords=pt)

    # previous value
    #hw.TypeKeys('l~p', pause=0.5)
    app.PopupMenu.MenuItem("Link To Excel->Previous Value").Click()

    #linkPrevious = app.window_(title_re = "Link Previous Value")
    #linkPrevious.Wait('exists', timeout = 5)
    #linkPrevious.Edit.SetText("69")

    #app.LinkPreviousValue.Wait('enabled')
    app.LinkPreviousValue.Edit.SetText(str(i))
    app.LinkPreviousValue.OK.Click()
    
    #xlapp.
    xlapp.top_window_().TypeKeys("^v~")
    
