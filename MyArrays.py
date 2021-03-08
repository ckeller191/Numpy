# read evaluate print loop - REPL
# activate repl in command palette to enter interactive mode
# you can't save it in the file, it is the interactive mode

import numpy as np
import random
 
integers = np.array([1,2,3]) 

#print(type(integers))

#print(integers)

#one dimensional array from a list comprehension that produces even integers from 2 - 20

integers = np.array([x for x in range(2,21,2)])

#print(integers)

#multi - dimensional

integers = np.array([[1,2,3],[4,5,6]])

#print(integers)

floats = np.array([0.0,0.1,0.2,0.3,0.4])
#print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size

print()

for row in integers:
    print(type(row))
    print(row)
    for col in row:
        print(col)

for i in integers.flat: # iterates through all values disregarding columns and rows
    print(i)



a1 = np.array([[random.randint(1,10) for i in range(5)], [random.randint(1,10) for i in range(5)]])

print(a1)

a2 = np.array(np.random.randint(1,10, size=(2,5)))

print(a2)



#default for these if float
c = np.zeros(5) # create an array of 5 elements of zeros
print(c)

d = np.ones(5) # create an array of 5 elements of ones
print(d)

e = np.ones((2,4), dtype=int) #create an array of 2 by 4 of ones of type int
print(e)

f = np.full((3,5),13) # 3x5 of 13s
print(f)

g = np.arange(5)
print(g)

g2 = np.arange(5,10) #lower and upper limits
print(g2)

g3 = np.arange(10,1,-2) #upper limit, lower limit, step value (here reverse)
print(g3)

h = np.linspace(0.0, 1.0, num=5) #evenly spaced float range
print(h)

array1 = np.arange(1,21)

array2 = array1.reshape(4,5)

print(array1, array2)


#python will compress data with '...' so we can see beginning and end of rows on screen
array3 = np.arange(1, 100001).reshape(4,25000)
print(array3)

array4 = np.arange(1, 100001).reshape(100,1000)
print(array4)


numbers = np.arange(1,6)

numbers += 10 # add 10 to each value in the array

print(numbers)


#BROADCASTING
print(numbers * 2)
#numbers * [2,2,2,2,2]


print(numbers ** 3)
#values of numbers not permanently changed - broadcasting inside print statement
print(numbers)

#multiplying integers with floating point arrays
numbers2 = np.linspace(1.1, 5.5, 5)
a = numbers * numbers2
print(a)

#comparing arrays - gives boolean true/false

print(numbers >= 13)

print(numbers2 < numbers)

print(numbers == numbers2)