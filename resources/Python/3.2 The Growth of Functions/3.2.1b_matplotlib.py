import matplotlib.pyplot as plt
import numpy as np

# Name
name = '3.2.1b'
title = 'x'

# Constant witnesses
C, k = 5, 4

# Hypothetical complexity
f = lambda x: 3*x + 7
ftext = 'f(x) = 3x + 7'

# Tightest bounding function for f(x)
g = lambda x: x
gtext = 'g(x) = %s'%title

# Input size
size = 25

# Coordinates for f(x) = y
x = np.array([x for x in range(0, size+1)])
y = np.array([f(x) for x in x])

# Coordinates for g(x)
g_x = np.array([g(x) for x in x])

# k Witness
vert = np.array([y for y in range(y[-1])])
w = np.array([k for y in vert])

plt.plot(x, y, label=ftext)
plt.plot(x, C*g_x, '--', label=gtext, alpha=0.7)
plt.plot(w, vert, '--', label='k = 4', color='grey', linewidth=1, alpha=0.4)
plt.title('f(x) is O(%s)'%title, loc='center')
plt.legend(loc=2)
plt.grid(linestyle=':', alpha=0.4)
plt.xlabel('Input')
plt.ylabel('Time')
plt.savefig(name+'_plot.jpg')
plt.show()
