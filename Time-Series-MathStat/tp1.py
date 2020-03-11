import numpy as np

a = np.array([1,2,3])
print(a)

a = np.array([[1,2],[3,4]])
print(a)

# minimum dimensions
a = np.array([1,2,3,4,5], ndmin=2)
print(a)

# dtype parameter
a = np.array([1,2,3], dtype=complex)
print(a)

# int8, int16, int32, int64 can be replaced by 'i1','i2','i4',etc...
dt = np.dtype('i4')
print(dt)

# using endian notation
dt = np.dtype('>i4')
print(dt)

student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype=student)
print(a)

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

# resize the ndarray
a.shape = (3,2)
print(a)

a = np.arange(24)
print(a)
print(a.ndim)
b = a.reshape(2,4,3)    # b is now three dimensions
print(b)
print(b.ndim)

# dtype of array is int8 (1 byte)
x = np.array([1,2,3,4,5], dtype=np.int8)
print(x.itemsize)   # returns the length of each element of array in bytes
x = np.array([1,2,3,4,5], dtype=np.float32)
print(x.itemsize)

# create an uninitialized array of specified shape and dtype
x = np.empty((3,2), dtype=int)
print(x)

# return array of specified size, filled with zeros
x = np.zeros((3,2), dtype=float)
print(x)

# or filled with ones
x = np.ones((3,2), dtype=int)
print(x)
x = np.ones(5)
print(x)
x = np.ones([2,2], dtype=int)
print(x)

#s = 'Hello World'
#a = np.frombuffer(s, dtype='S1')
#print(a)

# obtain iterator object from list
lst = range(5)
print(lst)
it = iter(lst)
# use iterator to create ndarray
x = np.fromiter(it, dtype=float)
print(x)

x = np.arange(5)
print(x)
x = np.arange(10,20,2)
print(x)

# linspace is like arange except instead of step size takes
# number of evenly spaced values between the interval
x = np.linspace(10,20,5)
print(x)
x = np.linspace(10,20,5, endpoint=False)
print(x)

# default base is 10
a = np.logspace(1.0, 2.0, num=10)
print(a)
# set base of log space to 2
a = np.logspace(1, 10, num=10, base=2)
print(a)


















