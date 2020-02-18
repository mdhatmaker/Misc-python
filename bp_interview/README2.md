# BP INTERVIEW FOLLOW-UP

The code associated with this document can be found in the "bp_interview" folder of my following public GitHub repo:
<https://github.com/mdhatmaker/Misc-python>


## Introduction

The following are some follow-up notes related to the BP face-to-face interview with Michael Hatmaker on Tue Feb 18, 2020:


## Performance

It appears that simple performance analysis can be done in a Jupyter notebook by using the 'timeit' keyword. Here is an example:
```
> timeit df['dates'] = pd.to_datetime(pd.Series(dates))
6.08 ms ± 57.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```


## Stock Data by Year

The "stock_price_by_year.ipynb" notebook is a better attempt at solving the problem of displaying the price charts for TSLA stock for each year. There are still a few things I find ugly (it's not perfect with leap year, etc.), but it's **much** better.

![tsla price chart][tsla_img]
[tsla_img]: ./TSLA_price_by_year.png "TSLA Stock Price"


## Decorators

I think I always assumed python decorators were just meta-data tags, so I never stopped to check them out. There are some *very* short samples in the "python_decorators.ipynb" notebook.


## Secure Access and Stored Images

I'm just starting to look at this now, but if I have an update ready before the EOD, I'll pass it along. I expect this to take a bit longer just because I want to evaluate a few different methods to see which one makes sense for this use case.


## Conclusion

Thanks again for your time today. I enjoyed meeting everyone, and I hope these updates add a little more to today's interview. Regardless, the questions were bugging me, and I had to figure them out.


## Other Resources

My website : <https://www.mdhatmaker.com>
My GitHub  : <https://github.com/mdhatmaker>
My LinkedIn: <https://www.linkedin.com/in/michael-hatmaker>


