import numpy as np

def funcion1():
    matrix=np.arange(0,50)
    diagonal = np.diagflat([matrix])
    np.save('exercici1.npy', diagonal)
    return diagonal

