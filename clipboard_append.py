import pyperclip



#append_to_begin = "BCHARTS,"
def append_beginning(append_to_begin):
    # get current clipboard contents
    spam = pyperclip.paste()

    # split the clipboard contents into a list of strings (by newline char)
    li = spam.split('\n')

    # create a new (empty) list
    li2 = []

    # add to newly created (empty) list the lines with the specified text appended
    for x in li:
        li2.append(append_to_begin + x)

    # recombine (separate with newline char)
    rejoin = '\n'.join(li2)

    # copy back to clipboard
    pyperclip.copy(rejoin)
    
    return



append_beginning('LOCALBTC,')
