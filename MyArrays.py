# read evaluate print loop - REPL
# activate repl in command palette to enter interactive mode
# you can't save it in the file, it is the interactive mode

import numpy as np
 
integers = np.array([1,2,3]) 

#print(type(integers))

#print(integers)

#one dimensional array from a list comprehension that produces even integers from 2 - 20

integers = np.array([x for x in range(2,21,2)])

#print(integers)

#multi - dimensional

integers = np.array([[1,2,3],[4,5,6]])

print(integers)

floats = np.array([0.0,0.1,0.2,0.3,0.4])
print(floats)