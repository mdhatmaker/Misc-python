from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import *


from download_crypto_historical import *


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
window.setWindowTitle('Download Crypto Historical Data')

layout = QVBoxLayout()  # Create a Vertical Layout to add all the widgets
#layout = QHBoxLayout()  # Create a Horizontal Layout to add all the widgets


label = QLabel('Select exchange and click Download')
layout.addWidget(label)

cboExchange = QComboBox()
cboExchange.addItem('gemini')
cboExchange.addItem('Coinbase')
cboExchange.addItem('Kraken')
cboExchange.addItem('Binance')
cboExchange.addItem('Bitstamp')
cboExchange.addItem('Bitfinex')
cboExchange.addItem('Cexio')
cboExchange.addItem('Itbit')
cboExchange.addItem('Poloniex')
layout.addWidget(cboExchange)

cboCrypto = QComboBox()
cboCrypto.addItem('BTC')
layout.addWidget(cboCrypto)

cboFiat = QComboBox()
cboFiat.addItem('USD')
layout.addWidget(cboFiat)

btn = QPushButton('Download')
layout.addWidget(btn)

txt = QLineEdit('(could be some text here)')
layout.addWidget(txt)

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

spinbox = QSpinBox()
layout.addWidget(spinbox)

tableWidget = QTableWidget()    #AvailableModules)
#tableWidget.resizeColumnsToContents()
tableWidget.setSelectionMode(QAbstractItemView.NoSelection)   #QtWidgets.QAbstractItemView.NoSelection)
tableWidget.setCornerButtonEnabled(True)
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

def on_cell_changed(item):
    print(item.text())
    #item.setForeground(QColor(255,0,0))
tableWidget.itemChanged.connect(on_cell_changed)

def on_cell_doubleclick(mi):
    row = mi.row()
    column = mi.column()
    #alert = QMessageBox()
    #alert.setText('You changed cells!\n')
    #alert.exec_()
    print('cell changed: {} {}'.format(row+1, column+1))
tableWidget.doubleClicked.connect(on_cell_doubleclick)  # cellChanged.connect(on_cell_changed)
#tableWidget.cellChanged.connect(on_cell_changed)
#tableWidget.itemChanged.connect(on_cell_changed)

def on_slider_change(value):
    print(value)
slider.valueChanged[int].connect(on_slider_change)

# gemini: BTCUSD, ZECUSD
# Coinbase: BTCUSD, LTCUSD, 
# Kraken: BTCUSD, ETHUSD, LTCUSD, XRPUSD, BTCEUR, ETHEUR, LTCEUR
# Binance: BTCUSDT, ETHUSDT, LTCUSDT, NEOUSDT
# Bitstamp: BTCUSD, ETHUSD, BTCEUR, ETHEUR, ...
# Bitfinex: BTCUSD, ETHUSD, LTCUSD, XRPUSD, BTCEUR, ETHEUR, LTCEUR, XRPEUR
# Cexio: BTCUSD, ETHUSD
# Itbit: BTCUSD
# Poloniex: BTCUSD, ETHUSD, LTCUSD, BCHUSD, XMRUSD, DASHUSD, ETCUSD
def on_index_changed_exchange(index):
    item = cboExchange.currentText()
    print(item)
    cboCrypto.clear()
    cboFiat.clear()
    cboFiat.addItem('USD')
    if item == 'gemini':
        cboCrypto.addItem('BTC')
        cboCrypto.addItem('ZEC')
    elif item == 'Coinbase':
        cboCrypto.addItem('BTC')
        cboCrypto.addItem('LTC')
    elif item == 'Kraken':
        cboCrypto.addItem('BTC')
        cboCrypto.addItem('ETH')
        cboCrypto.addItem('LTC')
        cboCrypto.addItem('XRP')
        cboFiat.addItem('EUR')
    elif item == 'Binance':
        cboCrypto.addItem('BTC')
        cboCrypto.addItem('ETH')
        cboCrypto.addItem('LTC')
        cboCrypto.addItem('NEO')
    elif item == 'Bitstamp':
        cboCrypto.addItem('BTC')
        cboCrypto.addItem('ETH')
        cboFiat.addItem('EUR')
    elif item == 'Bitfinex':
        cboCrypto.addItem('BTC')
        cboCrypto.addItem('ETH')
        cboCrypto.addItem('LTC')
        cboCrypto.addItem('XRP')
        cboFiat.addItem('EUR')
    elif item == 'Cexio':
        cboCrypto.addItem('BTC')
        cboCrypto.addItem('ETH')
    elif item == 'Itbit':
        cboCrypto.addItem('BTC')
    elif item == 'Poloniex':
        cboCrypto.addItem('BTC')
        cboCrypto.addItem('ETH')
        cboCrypto.addItem('LTC')
        cboCrypto.addItem('BCH')
        cboCrypto.addItem('XMR')
        cboCrypto.addItem('DASH')
        cboCrypto.addItem('ETC')
cboExchange.currentIndexChanged.connect(on_index_changed_exchange)

def on_button_clicked():
    #alert = QMessageBox()
    #alert.setText('You clicked the button!\n' + txt.text())
    #alert.exec_()
    cboExchangeText = str(cboExchange.currentText())
    cboCryptoText = str(cboCrypto.currentText())
    cboFiatText = str(cboFiat.currentText())
    txt.setText('Download: {}'.format(cboExchangeText))
    progress.setValue(25)
    #filename = get_crypto_historical_filename('Coinbase', 'BTC', 'USD')
    filename = get_crypto_historical_filename(cboExchangeText, cboCryptoText, cboFiatText)
    url = get_cryptodatadownload_url(filename)
    print("Reading {} from folder {}".format(filename, folder))
    download_file(url, folder)
    progress.setValue(75)
    df = read_historical(filename, folder, parserDateOnly)
    progress.setValue(100)
    #print(df.tail(50))
    print(df.head(20))
btn.clicked.connect(on_button_clicked)

def on_spin_changed():
    tableWidget.clearSelection()
    x = spinbox.value()
    #y = self.cbox.value()
    #self.table.setRangeSelected(QTableWidgetSelectionRange(x, y, x, y), True)
    print(x)
spinbox.valueChanged.connect(on_spin_changed)

window.setLayout(layout)
window.show()

app.exec_()
