#Matplotlib practice

import numpy as np
import matplotlib.pyplot as plt
# Functional Method
x = np.linspace(0,10,20)
y = x**2
plt.subplot(2,2,1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Functional Method')
plt.plot(x,y,'r-')

plt.subplot(2,2,2)
plt.ylabel('y')
plt.xlabel('x')
plt.title('Functional Method')
plt.plot(y,x,'b-')

plt.subplot(2,2,3)
plt.ylabel('y')
plt.xlabel('x')
plt.title('Functional Method')
plt.plot(x/4,y**3,'g-')

plt.subplot(2,2,4)
plt.ylabel('y')
plt.xlabel('x')
plt.title('Functional Method')
plt.plot((y/10)**3,x/4,'y-')

plt.show()
