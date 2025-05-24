##List: An ordered sequence of elements enclosed in square brackets, allowing heterogeneous elements (different data types).
# It is dynamic in size, meaning you can add/remove elements as needed.
##Array: An ordered sequence of elements enclosed in square brackets (when printed)
# but it only allows homogeneous elements (same data type). You need to import the array module, and its size is fixed
##lists are more flexible and faster for general-purpose operations, while arrays are optimized for numerical computations.
## ADVANTAGES
# Contiguous memory means data is stored in a single,continuous block of memory without any gaps between elements
# Memory efficiency
L1=[1,2,3]
import array
# Creating an integer array
arr = array.array('i', L1)
print(arr) # array('i', [1, 2, 3])

# Adding an element to the array
arr.append(4)

# Attempting to add a string would raise an error because arrays require homogeneous elements
# arr.append('5')  # This will cause an error

print(arr) #array('i', [1, 2, 3, 4])

# Removing an element from the array
arr.remove(3)
print(arr) ##array('i', [1, 2, 4])

# Inserting an element at a specific index
arr.insert(0, 22) # array('i', [22, 1, 2, 4])
print(arr)

# Retrieving the index position of an element
print(arr.index(22)) # 0

print(type(arr))  # <class 'array.array'>

from array import *

arr=array('i',[1,2,3,4,5,-6])

## function is used to return the type code of an array with which you are working.
print(arr.typecode)

#function gives you the size of an array and address of the array.
print(arr.buffer_info())


arr = array('i', [1, 2, 3, 4, 5, -6])

# Create a new array with squares of elements in arr
arr1 = array(arr.typecode, (i**2 for i in arr))

# --- For loop ---
for j in arr1:
    print(j)

# --- While loop ---
i = 0
while True:
    if len(arr1) == i:
        break
    else:
        print(arr1[i])
        i += 1
## Numpy
from numpy import *

# linspace() - it is used to create an array with equal interval between the elements
print(linspace(0,15,16)) # here it will break the range into 16 equal parts
#O/p :- [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]

print(linspace(0,15)) # by default it will break into 50 parts


# arange() - it will create an array with start value and end value with step size
print(arange(0,10,2)) # [0 2 4 6 8]


# logspace() -
print(logspace(1,40,5))

# zeros()
print(zeros(5)) # [0. 0. 0. 0. 0.]
print(zeros(5,int)) # [0 0 0 0 0]

# ones()
print(ones(6)) # [1. 1. 1. 1. 1. 1.]
print(ones(6,int)) # [1 1 1 1 1 1]


## Adding two arrays
arr1=array([2,4,6,8])
arr2=array([8,6,4,2])
print(arr1+arr2) # [10 10 10 10]


## Shallow copy -- > It will Affect the orginal list because both address is same

arr1=array([2,3,4])
arr2=arr1
print(arr1) # [2 3 4]
print(arr2) # [2 3 4]
print(id(arr1)) # 2309744473840
print(id(arr2)) # 2309744473840
arr1[2]=22 # Modifying the value in arr1
print(arr1) # [ 2  3 22]
print(arr2) # [ 2  3 22]

## Deep Copy :- It will not Affect the orginal list

arr1=array([2,3,4])
arr2=arr1.copy()
print(arr1) # [2 3 4]
print(arr2) # [2 3 4]
print(id(arr1)) # 2121712814096
print(id(arr2)) # 2121713236080
arr1[2]=22 # Modifying the value in arr1
print(arr1) # [ 2  3 22]
print(arr2) # [2 3 4]

# NumPy is ideal for handling multi-dimensional arrays efficiently

# dtype attribute returns the data type of the data with which you are working.
# ndim attribute gives the number of dimensions of an array
# reshape attribute is used to change the dimensions of an array. We can convert a 1-D array to a 2-D array by using the reshape method.
# reshape(r,c) method takes two parameters ie., the number of rows and a number of columns, that you want in an updated array.
# reshape attribute also works with a 3-D array. In 3-D, we have multiple 2-D arrays. And a 2-D array contains multiple 1-D arrays.
#matix() attribute is used to convert an array into a matrix format.
#We can also create a matrix without using an array. It can also be created directly by using the matrix() attribute.
 # matrix('1 2  3 6 ; 4 5 6 7')
## 1D array
arr= array([1,2,3,4,5])
print(arr)

## Square 1D array
arr1=array([i**2 for i in arr],'i') # 'i' specifies integer type
print(arr1)
## It will provide the dimensional of the array
print(arr.ndim)

## 2D array

# Two- dimensional array can be defined as an array within another array.
# When an array contains another array inside it, then it is known as a two-dimensional array.

m1=matrix('1,2,3,4,9,10;5,6,7,8,11,12')
print(m1)
print(m1.ndim) # 2
print(m1.flatten()) # [[1 2 3 4 5 6 7 8]]

## 3D array , converting above 2D array to 3D array

m1=array(matrix('1,2,3,4,9,10;5,6,7,8,11,12'))
m2=m1.reshape(2,2,3)
print(m2)

## Multiplying 2 matrix lists

L=[
    [1,2,3],
   [4,5,6]
   ]
L1=[
    [1,2],
    [3,4],
    [5,6]
    ]

## We need multiply only in case if rows of L equall to Colums of L1 else Matrix multiplication not possible
L2=[[0,0],[0,0]]
for i in range(0,len(L)):
    for j in range(len(L1[0])):
        for k in range(len(L1)):
            L2[i][j]+=L[i][k]*L1[k][j]
print(L2)
