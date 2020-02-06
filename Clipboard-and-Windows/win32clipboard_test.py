import win32clipboard as clip

"""
# set clipboard data
clip.OpenClipboard()
clip.EmptyClipboard()
clip.SetClipboardText('testing 123')
clip.CloseClipboard()
"""

# get clipboard data
clip.OpenClipboard()
data = clip.GetClipboardData()
clip.CloseClipboard()
print(data)
