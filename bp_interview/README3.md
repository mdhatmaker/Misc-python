# BP INTERVIEW FOLLOW-UP #2

The code associated with this document can be found in the "bp_interview" folder of one of my public GitHub repo:
<https://github.com/mdhatmaker/Misc-python/tree/master/bp_interview>


## Introduction

The following are some additional follow-up notes related to the BP face-to-face interview with Michael Hatmaker on Tue Feb 18, 2020.

Most code can be found in the '*.ipynb' files in this "bp_interview" folder.

The sample Flask app code is located in the "Flask_Blog" folder.


## F-Strings

There was a question about why I couldn't use 'f-string' formatting for python strings, and this appears to be available only in python versions 3.6 and above. F-string formatting lets you place variable names within curly braces:
```
> a = 10
> b = "hello"
> print(f'Number is {a} and string is {b}.')
Number is 10 and string is hello.
```


## Threading, Multiprocessing, Subprocesses

I coded out some samples of the various parallel processing methodologies. These can be found in the "parallel_processing.ipynb" file.


## OOP

I added a "bp_interview/Oop_Samples" folder to demonstrate how I typically use object-oriented design in python projects. As I mentioned, I tend to use them to represent relatively small CS data structures.


## Secure Access and Stored Images (Flask)

The "bp_interview/Flask_Blog" folder contains a sample Flask project that demonstrates some of the concepts we discussed in the interview (web forms, nicely-formatted web pages, security, etc.) This will be the project I expand to display various pre-built MatPlotLib (or perhaps Plotly) charts.

If you have the appropriate Flask-related libraries installed, you can launch the Flask_Blog project from the command line:
1. (change to the Flask_Blog directory)
2. export FLASK_APP=flaskblog.py
3. flask run


## Conclusion

This gets a little further in detailing some of my interview answers that I felt needed more explanation.


## Other Resources

My website : <https://www.mdhatmaker.com>
My GitHub  : <https://github.com/mdhatmaker>
My LinkedIn: <https://www.linkedin.com/in/michael-hatmaker>


