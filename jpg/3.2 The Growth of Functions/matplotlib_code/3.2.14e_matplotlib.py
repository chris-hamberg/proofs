from math import floor, ceil, log
import matplotlib.pyplot as plt
import numpy as np

# Name
name = '3.2.14e'
title = '3^x'

# Constant witnesses
C, k = 1, 1

# Hypothetical complexity
f = lambda x: x**3
ftext = 'f(x) = x^3'
cftext = 'C|f(x)|'

# Bounding function for f(x)
g = lambda x: 3**x
gtext = 'g(x) = %s'%title
cgtext = 'C|g(x)|'

# Input size
size = 5

# Coordinates for f(x) = y
x = np.array([x for x in range(1, size+1)])
y = np.array([f(x) for x in x])

# Coordinates for g(x)
g_x = np.array([g(x) for x in x])

# k Witness
vert = np.array([y for y in range(floor(y[-1]))])
w = np.array([k for y in vert])

#plt.plot(x, C*y, '--', color='blue', label=cftext, alpha=0.5)
plt.plot(x, y, color='blue', label=ftext)

plt.plot(x, g_x, '--', color='green', label=gtext, alpha=0.5)
#plt.plot(x, C*g_x, '--', color='green', label=cgtext, alpha=0.5)

#plt.plot(x, C*y, '--', color='blue', label=cftext, alpha=0.4)

#plt.plot(w, vert, '--', label='k = %d'%k, color='grey', linewidth=1, alpha=0.4)
plt.title('f(x) is O(g(x)) (%s)'%name, loc='center')
plt.legend(loc=2)
plt.grid(linestyle=':', alpha=0.4)
plt.xlabel('Input')
plt.ylabel('Time')
plt.savefig(name+'_plot.jpg')
plt.show()
