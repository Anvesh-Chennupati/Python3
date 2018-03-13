#Object Oriented Approach
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.linspace(0,10,20)
y = x**2
axes = fig.add_axes([0.1,0.1,1,1])
#axes.plot(x,y)
axes2 = fig.add_axes([0.2,0.2,0.2,0.2])
axes2.plot(x,y)
axes3 = fig.add_axes([0.4,0.2,0.2,0.2])
axes3.plot(x,y)
axes4 = fig.add_axes([0.6,0.2,0.2,0.2])
axes5 = fig.add_axes([0.8,0.2,0.2,0.2])
axes6 = fig.add_axes([0.2,0.4,0.2,0.2])
axes7 = fig.add_axes([0.2,0.6,0.2,0.2])
axes8 = fig.add_axes([0.2,0.8,0.2,0.2])
#axes8 = fig.add_axes([0.2,0.2,0.2,0.2])
plt.show()
