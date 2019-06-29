from Tkinter import Tk
import win32clipboard
import re

# pass in the lines of text (as a list)
def replace_tilda(textList):    
    revisedLines = list()
    for ln in textList:
        # empty strings are False
        line = ln.strip()
        if line:
            p = re.compile(' ~')
            # unicode 2014 is emdash
            revised = '"' + p.sub(u'" \u2014', line)
            revisedLines.append(revised)
    return revisedLines

# get clipboard contents
def get_clipboard_text():
    return paste()
    #r = Tk()
    #result = r.selection_get(selection="CLIPBOARD")
    #r.destroy()
    #return result

# set clipboard contents
def set_clipboard_text(text):
    copy(text)
    return
    #r = Tk()
    #r.withdraw()
    #r.clipboard_clear()
    #r.clipboard_append(text)
    #r.destroy()
    #return

def copy(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return

def paste():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data

# get the clipboard contents split into text lines
def get_clipboard_lines(remove_blank):
    lines = get_clipboard_text().split('\n')
    revisedLines = list()
    for i in range(0, len(lines)):
        if (lines[i].strip() or (not remove_blank)):
            revisedLines.append(lines[i].strip())
    return revisedLines

def set_clipboard_lines(textList):
    text = ""
    for line in textList:
        text = text + line + "\n"
    set_clipboard_text(text)
    return
    
# print the contents of a list    
def print_list(outputList):
    for item in outputList:
        print item
    return

##############################################################################

#lines = list(open("testquotes.txt"))
#updated = replace_tilda(lines)
#print_list(updated)

lines = get_clipboard_lines(True)
#print lines
updated = replace_tilda(lines)
print_list(updated)

set_clipboard_lines(updated)
#set_clipboard_text("hello nonsense")
print "CLIP: " + get_clipboard_text()

