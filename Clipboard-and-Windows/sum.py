#!/usr/bin/python 
# -*- coding: cp1252 -*-
# my simple python summation app,  
# gets 2 integers and returns the sum 
#
# *** THIS PYTHON SCRIPT IS USED TO TEST CALLING PYTHON FROM C# ***
# https://code.msdn.microsoft.com/windowsdesktop/C-and-Python-interprocess-171378ee

import sys 
 
x = int(sys.argv[1])  
y = int(sys.argv[2]) 
 
print x+y
