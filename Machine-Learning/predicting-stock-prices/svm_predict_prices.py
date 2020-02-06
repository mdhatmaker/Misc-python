import csv
import numpy as np
from sklearn.svm import SVR
from os.path import join
#import matplotlib.pyplot as plt
from datetime import datetime
import sys

#plt.switch_backend('new_backend')


historical_data_path = r"/Users/michael/Dropbox/MyProjects/python/_data"
def get_data(symbol):
    dates = []
    prices = []
    filename = join(historical_data_path, symbol + ".csv")
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            date_ = row[0]
            open_ = float(row[1])
            print row[0]
            print row[1]
            high_ = float(row[2])
            low_ = float(row[3])
            close_ = float(row[4])
            volume_ = int(row[5])
            prices.append(float(close_))
            #dt = datetime.strptime(date_, "%Y-%m-%d")
            #timespan = (dt - datetime(2002,1,1))
            #dates.append(int(timespan.days))
            dates.append(int(row[0].split('-')[0]))
    return (dates, prices)

def plot(dates, prices):
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='red', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
    return

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))
    # Support Vector Regression
    # - uses space between data points as a margin of error and
    # - predicts the most-likely next point in a dataset
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

################################################################################

print "Getting historical data..."
(dates, prices) = get_data('AAPL')
print "Predicting prices..."
predicted_price = predict_prices(dates, prices, 29)
print "Done."
print(predicted_price)


    
