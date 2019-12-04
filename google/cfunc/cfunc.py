import sys
import ctypes 

# https://www.geeksforgeeks.org/how-to-call-a-c-function-in-python/

"""
    int myFunction(int num) 
    { 
        if (num == 0) 
    
            // if number is 0, do not perform any operation. 
            return 0; 
        else
            // if number is power of 2, return 1 else return 0 
            
        num & (num - 1) == 0 ? return 1 : return 0 
    }
    # cc -fPIC -shared -o libfun.so function.c
"""

def test_c_function():
    NUM = 16      
    # libfun loaded to the python file 
    # using fun.myFunction(), 
    # C function can be accessed 
    # but type of argument is the problem. 
                            
    fun = ctypes.CDLL('./libfun.so')  
    # Now whenever argument  
    # will be passed to the function                                                         
    # ctypes will check it. 
    
    fun.myFunction.argtypes(ctypes.c_int) 
    
    # now we can call this  
    # function using instant (fun) 
    # returnValue is the value  
    # return by function written in C  
    # code 
    returnValue = fun.myFunction(NUM) 
    print(returnValue)


if __name__ == "__main__":
    
    test_c_function()
