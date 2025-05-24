##List: An ordered sequence of elements enclosed in square brackets, allowing heterogeneous elements (different data types).
# It is dynamic in size, meaning you can add/remove elements as needed.
##Array: An ordered sequence of elements enclosed in square brackets (when printed)
# but it only allows homogeneous elements (same data type). You need to import the array module, and its size is fixed
##lists are more flexible and faster for general-purpose operations, while arrays are optimized for numerical computations.
## ADVANTAGES
# Contiguous memory means data is stored in a single,continuous block of memory without any gaps between elements
#Memory Efficency
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
##
# L=[1,2,3,4,5,'6']
#
# import numpy as np
#
# mixed_array = np.array(L)
# print(type(mixed_array))
# print(mixed_array)
a=2
print(a)