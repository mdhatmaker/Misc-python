# Sample python project for BP interview

The code mentioned in this document is available in the 'bp_interview' folder of the following public GitHub repo:
<https://github.com/mdhatmaker/Misc-python>


## Introduction

In order to make it easier to evaluate whether I'm a good fit with BP, I wrote some very simple sample code in python. I thought perhaps going through this code would allow us a more efficient interview.

## Overview

I was told the technologies BP is interested in would include the following:
-Python
-Pandas
-NumPy
-Flask
-Jupyter
-APIs
-REST

The code I created for this interview should cover most of these with the obvious exceptions of Flask and Jupyter. In reference to these two, I have used Jupyter (very cool), and I did a quick read-through of Flask. Although I have not used Flask previously, it seems pretty straightforward (and also very cool as a way to quickly implement python-based web pages). 

The code to run is the 'sample.py' file. This imports functionality from the 'get_historical.py' and 'get_report_data.py' files.

This project pulls info from online EIA crude oil stocks reports, and it also pulls crude price data using the Quandl library. It then plots a small subset using MatPlotLib. Originally, the code pulled the EIA data directly from the website, but this eventually caused an error from too many requests. To solve this, I created a 'data' folder where I download the EIA reports just once, and I subsequently read these CSV files into a pandas dataframe.

Because this was a sample that I put together very quickly, it will be missing some fundamentals such as error-handling and unit tests.

## Conclusion

This is a very simple demonstration of pulling some energy-related data from an online source, using Quandl to retrieve historical prices, and plotting with MatPlotLib.

I only spent part of a day on this, and there is certainly more I'd like to implement, including the following:
-add other EIA report data
-scrape EIA web page with BeautifulSoup to pull all available report dates
-add API report data (currently has EIA only)
-store data files (i.e. CSV dataframe files) in the cloud rather than local
-do some machine-learning price prediction with TensorFlow (I just began exploring this, which explains the 'tf2' folder)

## Other Projects

Almost all of my GitHub repos are public, but in particular, the 'Trading-prime-python' repo contains more of the python work I did recently for use in analyzing index, futures, and cryptocurrency data:
<https://github.com/mdhatmaker/Trading-prime-python>

