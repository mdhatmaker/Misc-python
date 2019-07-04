from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import *


app = QApplication([])
app.setStyle('Fusion')
#app.setStyle('Windows')
#app.setStyle('Macintosh')

# change app appearance via (Qt) style sheets
app.setStyleSheet("QPushButton { margin: 5ex; }")

# Change widget colors for all widgets of a certain type
#palette = QPalette()
#palette.setColor(QPalette.ButtonText, Qt.red)
#app.setPalette(palette)


window = QWidget()
layout = QVBoxLayout()  # Create a Vertical Layout to add all the widgets
#layout = QHBoxLayout()  # Create a Horizontal Layout to add all the widgets

window.setWindowTitle('My App Description')

label = QLabel('Hello world')
#label.show()
layout.addWidget(label)

btn = QPushButton('click me')
#btn.show()
layout.addWidget(btn)

txt = QLineEdit('edit me, bitch')
layout.addWidget(txt)

cbo = QComboBox()
cbo.addItem('item 1')
cbo.addItem('item 2')
layout.addWidget(cbo)

chk = QCheckBox('Qt checkbox')
chk.setChecked(False)
layout.addWidget(chk)

rdo = QRadioButton()
layout.addWidget(rdo)

#slider = QSlider()
#layout.addWidget(slider)
slider = QSlider(Qt.Horizontal)   #, self)
#mySlider.setGeometry(30, 40, 200, 30)
layout.addWidget(slider)

progress = QProgressBar()
progress.setMinimum(0)
progress.setMaximum(100)
layout.addWidget(progress)

#tbl = QTableWidget()
#tbl.add
tableWidget = QTableWidget()    #AvailableModules)
#tableWidget.resizeColumnsToContents()
tableWidget.setSelectionMode(QAbstractItemView.NoSelection)   #QtWidgets.QAbstractItemView.NoSelection)
tableWidget.setCornerButtonEnabled(True)
#tableWidget.setRowCount(0)
#tableWidget.setColumnCount(3)
tableWidget.setRowCount(4)
tableWidget.setColumnCount(2)
tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
tableWidget.move(0,0)
tableWidget.setObjectName("table_1")
tableWidget.horizontalHeader().setSortIndicatorShown(False)
tableWidget.horizontalHeader().setStretchLastSection(True)
tableWidget.verticalHeader().setVisible(False)
layout.addWidget(tableWidget)


def changeValue(value):
    print(value)
slider.valueChanged[int].connect(changeValue)

def on_button_clicked():
    #alert = QMessageBox()
    #alert.setText('You clicked the button!\n' + txt.text())
    #alert.exec_()
    txt.setText('You Clicked!!!')
    progress.setValue(50)
btn.clicked.connect(on_button_clicked)

window.setLayout(layout)
window.show()

app.exec_()
