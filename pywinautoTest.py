from pywinauto import application

#app = pywinauto.application.Application.start('notepad.exe')
#app.start_('notepad.exe')
#app.Notepad.MenuSelect('help->aboutnotepad')

app = application.Application()
app.Autotrader.print_control_identifiers()
app.ON.Click()
