import numpy as np

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
