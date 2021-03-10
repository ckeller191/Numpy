import numpy as np
import random
grades = np.array([[87,96,70], [100,87,90], [94,77,90], [100,81,82]])

#ROWS - grades for each student
#COLUMNS - grades on each test

a = grades.sum()
b=grades.min()
c=grades.max()
d=grades.mean()
e=grades.std()
f=grades.var()

g = grades.mean(axis=0) #by column for every row
print("Average of each test", g)

h = grades.mean(axis=1) #by row for every column
print("Average for each student", h)


numbers = np.array([1,4,9,16,25,36])

sqrt = np.sqrt(numbers)

print(sqrt)

numbers2 = np.arange(1,7)*10
#makes an array counting by 10, 10-60 - 7 tells it where to stop, so no 70

add = np.add(numbers, numbers2)

print(add)

multiply = np.multiply(numbers2, 5)

print(multiply)

numbers3 = numbers2.reshape(2,3)

print(numbers3)

numbers4 = np.array([2,4,6])

multiply2 = np.multiply(numbers3, numbers4)

print(multiply2)


#Indexing and Slicing

grades = np.array([[87,96,70], [100,87,90], [94,77,90], [100,81,82]])


a = grades[0,1]
#gives 96
print(a)

b = grades[1]
#array of second row - ([100, 87, 90])

#To select multiple sequential rows
firsttwo = grades[0:2]
#first two rows - doesn't include upper limit

#Select multiple non-squential rows
print(grades[[1, 3]])

#all rows and only first column
c = grades[:,0]
print(c)
#output - [87, 100, 94, 100]


#select consecutive columns using a slice
d = grades[:,1:3]
#can drop the 3 - only 3 columns, so no fourth column to include anyway
print(d)


e = grades[:, [0,2]]
#selects first and third columns of all rows
print(e)

grades2 = np.array([random.randint(60,100) for i in range(12)])
print(grades2)

grades3 = grades2.reshape(3,4)

print(grades3)

avg = grades3.mean()

avg_test = grades3.mean(axis=1)

avg_stu = grades3.mean(axis=0)

print(avg)
print(avg_test)
print(avg_stu)

#MORE EFFICIENT METHOD - do this

grades = np.random.randint(60,101,12).reshape(3,4)

print(grades)

print(grades.mean())

print(grades.mean(axis=0))

print(grades.mean(axis=1))


#Shallow copies (view) - array method view returns a new array object with a view of the original array

numbers = np.arange(1,6)
#array([1,2,3,4,5])

numbers2 = numbers.view()
#same elements as original array

numbers[1] *= 10

print(numbers2)


#changing value in the view also changes the value in original array

numbers2[1] /= 10

print(numbers)


#slice views
#slices also create views. lets make numbers2 a slice that views only the first
#three elements of numbers

numbers2 = numbers[0:3]

numbers[1] *= 20

print(numbers2)







#Deep copies (copy)
#the array method copy returns a new array object with a deep
#copy of the original array
numbers = np.arange(1,6)

numbers2 = numbers.copy()
#creates a new, independent array

numbers[1] *= 10
#numbers2 unaffected by change; numbers2 is a copy, its own new array
print(numbers2)

#reshape method returns a view (shallow copy) of the original array with the new dimensions; original not modified

grades = np.array([[87,96,70], [100,87,90]])

a = grades.reshape(1,6)

b = grades.resize(1,6)
#resize method made permanent change to grades

print(a)
print(grades)
#now the same thing, grades got resized in b

#Method flatten deep copies the original array's data:

flattened = grades.flatten()
print(flattened)

#ravel method produces a view (shallow copy) of original array which shares its data
raveled = grades.ravel()
print(raveled)

raveled[0] = 100 #updates grades so that 1st value is now 100


print(grades)

#you can quickly transpose an arrays rows and columns to "flip" the array, so the rows
#become the columns and the columns become the rows
#the T attribute returns a transposed view (shallow copy) of the array

transposed = grades.T
print(transposed)


#HSTACK - lets assume grades2 represents three additional exam grades for the students in the grades array

grades = np.array([[87,96,70], [100,87,90]])
grades2 = np.array([[94,77,90], [100, 81,82]])

h_grades = np.hstack((grades, grades2))
#new array
print(h_grades)

#VSTACK

#lets assume grades2 represents two more students' grades on three exams

v_grades = np.vstack((grades, grades2))
print(v_grades)