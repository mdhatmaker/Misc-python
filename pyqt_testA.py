import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.setWindowIcon(QtGui.QIcon('C:/Users/mhatmaker/Pictures/icons/down-arrow-circle-16.png'))

    btn = QtGui.QPushButton('Button', w)
    btn.resize(btn.sizeHint())
    btn.move(50, 50)

    btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
    
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
