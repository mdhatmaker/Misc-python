"""
from statsmodels.tsa.arima_model import _arma_predict_out_of_sample     # this is the nsteps ahead predictor function
import statsmodels.api as sm

data = [1,5,6,2,4,8, 6, 5, 5, 6, 2, 1, 9, 10, 1, 2, 1, 6, 4, 5, 6, 7]
data = [float(x) for x in data]

arma = sm.tsa.ARMA(data, order =(1,0))
results = arma.fit( full_output=False, disp=0)
# Where data is a one-dimensional array. To get in-sample predictions:
pred = results.predict()
"""

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt


# Warnings ignored for this code to avoid a lot of noise from running the procedure.
# This can be done as follows:
import warnings
warnings.filterwarnings("ignore")


"""
# load dataset
def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')
"""

def test1():
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # split into train and test sets
    X = series.values
    train, test = X[0:-12], X[-12:]
    history = [x for x in train]
    predictions = list()
    # walk-forward validation
    for t in range(len(test)):
        # fit model
        model = ARIMA(history, order=(4,1,0))
        model_fit = model.fit()
        # one step forecast
        yhat = model_fit.forecast()[0]
        # store forecast and ob
        predictions.append(yhat)
        history.append(test[t])
    # evaluate forecasts
    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)
    # plot forecasts against actual outcomes
    pyplot.plot(test)
    pyplot.plot(predictions, color='red')
    pyplot.show()
    return

# evaluate an ARIMA model for a given order (p,d,q)
def evaluate_arima_model(X, arima_order):
    # prepare training dataset
    train_size = int(len(X) * 0.66)
    train, test = X[0:train_size], X[train_size:]
    history = [x for x in train]
    # make predictions
    predictions = list()
    for t in range(len(test)):
            model = ARIMA(history, order=arima_order)
            model_fit = model.fit(disp=0)
            yhat = model_fit.forecast()[0]
            predictions.append(yhat)
            history.append(test[t])
    # calculate out of sample error
    error = mean_squared_error(test, predictions)
    return error

# EVALUATE A GRID OF ARIMA HYPERPARAMETERS
# evaluate combinations of p, d and q values for an ARIMA model
def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p,d,q)
                try:
                    mse = evaluate_arima_model(dataset, order)
                    if mse < best_score:
                            best_score, best_cfg = mse, order
                    print('ARIMA%s MSE=%.3f' % (order,mse))
                except:
                    continue
    print('Best ARIMA%s MSE=%.3f' % (best_cfg, best_score))

# We can use a custom date-parsing function when loading the data and baseline
# the year from 1900, as follows:
# load dataset
def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')


def grid_search():
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)

    # evaluate parameters
    p_values = [0, 1, 2, 4, 6, 8, 10]
    d_values = range(0, 3)
    q_values = range(0, 3)
    warnings.filterwarnings("ignore")
    evaluate_models(series.values, p_values, d_values, q_values)
    return



grid_search()







