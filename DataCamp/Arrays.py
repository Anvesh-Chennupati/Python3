
import numpy as np

val = [1,2,3,4,4,5,6,7,7,8]

val = val + val

new_val = val[:]

print(val * 2)

print(new_val)

np_val = np.array(val)

np_val = np_val * 2

print(np_val)
