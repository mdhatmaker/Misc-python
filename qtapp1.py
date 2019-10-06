#from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import *

app = QApplication([])

label = QLabel('Hello World!')
label.show()

button = QPushButton('Click')
# in Python, any function can be a 'slot' (C++ slots must be declared in a special way)
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)   # button.clicked is a signal
button.show()

app.exec_()
