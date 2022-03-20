import numpy as np
import math as ma

def func(arg):
    result=0
    for i in arg:
        result =ma.sin(i/2)*ma.exp(-i/4)+2*ma.exp(-i/2)
        print(result,end = ' ')
func(np.array([float(i) for i in input().split()]))


