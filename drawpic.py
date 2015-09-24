import numpy as  np
import matplotlib.pyplot as plt

x=np.linspace(0.0, 10.0,100)
y=np.sin(x)
z=np.cos(x)

plt.xkcd()

plt.plot(x,y,x,z)
plt.xlabel('my x var')
plt.ylabel('my y var')
plt.title('title')