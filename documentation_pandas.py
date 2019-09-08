# We work with rolling, expanding and exponentially weighted data through the corresponding objects,
# Rolling, Expanding and EWM.
# (where s is a series...)
# r = s.rolling(window=60)      # r is Rolling [window=60,center=False,axis=0]
# Available properties and methods:
# r.agg         r.apply     r.count     r.exclusions    r.max       r.median
# r.aggregate   r.corr      r.cov       r.kurt          r.mean      r.min
# To use a different "frequency" on rolling data, you can simply resample the input prior to creating a window function.
# For example, to get the max value on a rolling 5 Day window, one could use r.resample('D').max().rolling(window=5).max(),
# which first resamples the data to daily data, then provides a rolling 5 day window.

