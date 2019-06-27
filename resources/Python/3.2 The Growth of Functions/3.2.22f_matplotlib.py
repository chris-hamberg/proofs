from math import factorial, floor, ceil, log
from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np

# Name
name = '3.2.22f'
title = 'x'

# Constant witnesses
C1, C2, k = 1, 0.5, 1

# Hypothetical complexity
f = lambda x: ceil(x/2)
ftext = 'f(x) = ceil(x/2)'
cftext = 'C|f(x)|'

# big Bounding function for f(x)
g = lambda x: x
gtext = 'g(x) = %s'%title
c1gtext = 'C1|g(x)| = %d|%s|'%(C1, title)
c2gtext = 'C2|g(x)| = {0:.1}|{1}|'.format(C2, title)

# Input size
size = 25

# Coordinates for f(x) = y
A = np.arange(0, size+1, 0.001)
x = np.array([x for x in A])
y = np.array([f(x) for x in x])

# Coordinates for g(x)
g_x = np.array([g(x) for x in x])

# k Witness
vert = np.array([y for y in range(floor(y[-1]))])
w = np.array([k for y in vert])

#plt.plot(x, C*y, '--', color='blue', label=cftext, alpha=0.5)
plt.plot(x, y, color='blue', label=ftext)

plt.plot(x, C1*g_x, '--', color='green', label=c1gtext, alpha=0.5)
plt.plot(x, C2*g_x, '--', color='green', label=c2gtext, alpha=0.5)
#plt.plot(x, C*y, '--', color='blue', label=cftext, alpha=0.4)

plt.plot(w, vert, '--', label='k = %d'%k, color='grey', linewidth=1, alpha=0.4)
plt.title('f(x) is big-Theta(g(x)) (%s)'%name, loc='center')
plt.legend(loc=2)
plt.grid(linestyle=':', alpha=0.4)
plt.xlabel('Input')
plt.ylabel('Time')
#plt.yscale('log')
plt.savefig(name+'_plot.jpg')
plt.show()
