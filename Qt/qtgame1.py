import sys
import time

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

#from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
#from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine


class Calculator(QObject):
    def __init__(self):
        QObject.__init__(self)

    # Signal sending sum
    # Necessarily give the name of the argument through arguments=['sum']
    # Otherwise it will not be possible to get it up in QML
    sumResult = pyqtSignal(int, arguments=['sum'])

    subResult = pyqtSignal(int, arguments=['sub'])

    # Slot for summing two numbers
    @pyqtSlot(int, int)
    def sum(self, arg1, arg2):
        # Sum two arguments and emit a signal
        self.sumResult.emit(arg1 + arg2)

    # Slot for subtraction of two numbers
    @pyqtSlot(int, int)
    def sub(self, arg1, arg2):
        # Subtract arguments and emit a signal
        self.subResult.emit(arg1 - arg2)



if __name__ == "__main__":

    # Create an instance of the application
    app = QGuiApplication(sys.argv)
    # Create a QML engine.
    engine = QQmlApplicationEngine()
    # Create a calculator object
    calculator = Calculator()
    # And register it in the context of QML
    engine.rootContext().setContextProperty("calculator", calculator)
    # Load the qml file into the engine
    engine.load("qtgame1.qml")

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())

    