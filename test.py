import numpy as np

c=[[1,2,3],[4,5,6],[7,8,9]]
print(np.cumsum(c,axis=0))
print("<<<<<<<<<<<<<<")
print(np.cumsum(c,axis=1))
"""
[[ 1  2  3]
 [ 5  7  9]
 [12 15 18]]
<<<<<<<<<<<<<<
[[ 1  3  6]
 [ 4  9 15]
 [ 7 15 24]]
"""