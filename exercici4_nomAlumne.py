import numpy as np

def funcion4():
    array = np.random.randint(80, size=(4, 3)) 
    array = np.resize(array,(3,4))
    array = array.T
    print(array)
    array[::,2] = array[0][2]
    return array



