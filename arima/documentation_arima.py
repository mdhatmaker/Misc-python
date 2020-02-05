"""
Good ARIMA websites:

http://www.seanabu.com/2016/03/22/time-series-seasonal-ARIMA-model-in-python/
http://ascratchpad.blogspot.com/2011/03/arima-forecasting-and-python.html
https://robjhyndman.com/hyndsight/longseasonality/
https://machinelearningmastery.com/grid-search-arima-hyperparameters-with-python/
https://machinelearningmastery.com/tune-arima-parameters-python/


"""

"""
These notes are/were relevant when converting Alvin's existing EasyLanguage code:
    # HERE IS THE DESCRIPTION OF EASYLANGUGAGE LINREGARRAY FUNCTION:
    # LinRegArray(PriceArray, Size, TgtPos, oLRSlope, oLRAngle, oLRIntercept, oLRValueRaw)
    #   The LinRegArray function itself returns a value of 1 (Integer).
    # PriceArray : NumericArray : Specifies the numeric array of data elements to evaluate.
    # Size : Numeric : Sets the number of elements (size) in the array to consider.
    # TgtPos : Numeric : Sets the point in the past or future to use for projecting a regression value. Use a positive integer for a previous point and a negative integer for a future point.
    # oLRSlope : Numeric : Outputs the slope of the linear regression line.
    # oLRAngle : Numeric : Outputs the angle of the linear regression line in degrees.
    # oLRIntercept : Numeric: Outputs the intercept value at which the linear regression line will intersect the last array element.
    # oLRValueRaw : Numeric : Outputs the regression value for a point TgtPos elements in the past or projected into the future.

    # So our forecast is always the oLRValueRaw output from linregarray (the regression value for the point at
    #forecast = v4;

    # Then we just plot the forecast in white and the average of "diff1" (for lookback datapoints) in yellow
    #plot1(forecast, "forecast", white);
    #plot2(xaverage(diff1, window), "avg", yellow);

    # HERE IS THE DESCRIPTION OF THE EASYLANGUAGE XAVERAGE FUNCTION:
    # XAverage(Price, Length)
    #   The XAverage function itself returns the (double) numeric value containing the EXPONENTIAL moving average over a specified number of bars.
    # Price : Numeric : Specifies which bar value (price, function, or formula) to use.
    # Length : Numeric : Sets the number of bars to consider.
"""


"""
If the keyword "typ" is passed to the predict method, the answer will be shown in the original predictor variables:
 'linear' : Linear prediction in terms of the differenced endogenous variables.
 'levels' : Predict the levels of the original endogenous variables.
"""


"""
The “disp” Parameter

The first parameter we will look at is the disp parameter.

This is described as follows:
If True, convergence information is printed. For the default l_bfgs_b solver, disp controls the frequency of the
output during the iterations. disp < 0 means no output in this case.

By default, this parameter is set to 1, which shows output.

We are dealing with this first because it is critical in removing all of the convergence output when evaluating
the ARIMA model using walk-forward validation.

Setting it to False turns off all of this noise.
"""


"""
The “transparams” Parameter

This parameter controls whether or not to perform a transform on AR parameters.

Specifically, it is described as:
Whether or not to transform the parameters to ensure stationarity. Uses the transformation suggested in
Jones (1980). If False, no checking for stationarity or invertibility is done.

By default, transparams is set to True, meaning this transform is performed.

This parameter is also used on the R version of the ARIMA implementation (see docs) and I expect this is
why it is here in statsmodels.

The statsmodels doco is weak on this, but you can learn more about the transform in the paper:
Maximum Likelihood Fitting of ARMA Models to Time Series With Missing Observations
http://www.tandfonline.com/doi/abs/10.1080/00401706.1980.10486171
"""

"""
https://machinelearningmastery.com/grid-search-arima-hyperparameters-with-python/

The ARIMA model for time series analysis and forecasting can be tricky to configure.

There are 3 parameters that require estimation by iterative trial and error from reviewing diagnostic plots
and using 40-year-old heuristic rules.

We can automate the process of evaluating a large number of hyperparameters for the ARIMA model by using a
grid search procedure.

We can automate the process of training and evaluating ARIMA models on different combinations of model
hyperparameters. In machine learning this is called a grid search or model tuning.

In this tutorial, we will develop a method to grid search ARIMA hyperparameters for a one-step rolling forecast.

The approach is broken down into two parts:
1. Evaluate an ARIMA model.
2. Evaluate sets of ARIMA parameters.


1. EVALUATE ARIMA MODEL
We can evaluate an ARIMA model by preparing it on a training dataset and evaluating predictions on a test dataset.

This approach involves the following steps:

1. Split the dataset into training and test sets.
2. Walk the time steps in the test dataset.
   A. Train an ARIMA model.
   B. Make a one-step prediction.
   C. Store prediction; get and store actual observation.
3. Calculate error score for predictions compared to expected values.

We can implement this in Python as a new standalone function called evaluate_arima_model() that takes a time
series dataset as input as well as a tuple with the p, d, and q parameters for the model to be evaluated.

The dataset is split in two: 66% for the initial training dataset and the remaining 34% for the test dataset.

Each time step of the test set is iterated. Just one iteration provides a model that you could use to make
predictions on new data. The iterative approach allows a new ARIMA model to be trained each time step.

A prediction is made each iteration and stored in a list. This is so that at the end of the test set, all
predictions can be compared to the list of expected values and an error score calculated. In this case,
a mean squared error score is calculated and returned.


2. ITERATE ARIMA PARAMETERS
Evaluating a suite of parameters is relatively straightforward.

The user must specify a grid of p, d, and q ARIMA parameters to iterate. A model is created for each parameter
and its performance evaluated by calling the evaluate_arima_model() function described in the previous section.

The function must keep track of the lowest error score observed and the configuration that caused it. This can
be summarized at the end of the function with a print to standard out.

We can implement this function called evaluate_models() as a series of for loops.

There are two additional considerations. The first is to ensure the input data are floating point values
(as opposed to integers or strings), as this can cause the ARIMA procedure to fail.

Second, the statsmodels ARIMA procedure internally uses numerical optimization procedures to find a set of
coefficients for the model. These procedures can fail, which in turn can throw an exception. We must catch
these exceptions and skip those configurations that cause a problem. This happens more often than you would think.

Additionally, it is recommended that warnings be ignored for this code to avoid a lot of noise from running the
procedure. This can be done as follows:
"""
#import warnings
#warnings.filterwarnings("ignore")

"""

EXTENDING THE ARIMA GRID SEARCH METHOD

The grid search method used in this tutorial is simple and can easily be extended.

This section lists some ideas to extend the approach you may wish to explore.

Seed Grid. The classical diagnostic tools of ACF and PACF plots can still be used with the results used to seed
the grid of ARIMA parameters to search.
Alternate Measures. The search seeks to optimize the out-of-sample mean squared error. This could be changed to
another out-of-sample statistic, an in-sample statistic, such as AIC or BIC, or some combination of the two. You
can choose a metric that is most meaningful on your project.
Residual Diagnostics. Statistics can automatically be calculated on the residual forecast errors to provide an
additional indication of the quality of the fit. Examples include statistical tests for whether the distribution
of residuals is Gaussian and whether there is an autocorrelation in the residuals.
Update Model. The ARIMA model is created from scratch for each one-step forecast. With careful inspection of the
API, it may be possible to update the internal data of the model with new observations rather than recreating it
from scratch.
Preconditions. The ARIMA model can make assumptions about the time series dataset, such as normality and stationarity.
These could be checked and a warning raised for a given of a dataset prior to a given model being trained.


"""


#model = tsa.arima_model.ARIMA(data, (12, 1, 0)).fit()
#arima_predict = model.predict('2015-01-01', '2016-01-01', typ='levels')
#model = ARIMA(df.y, order=(0, 1, 0))
#model_fit = model.fit()



