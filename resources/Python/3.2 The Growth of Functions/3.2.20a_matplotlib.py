from math import factorial, floor, ceil, log
import matplotlib.pyplot as plt
import numpy as np

# Name
name = '3.2.20a'
title = 'n^3 log n'

# Constant witnesses
C, k = 27, 10

# Hypothetical complexity
f = lambda n: (
        (((n**3) + (n**2) * log(n)) * (log(n) + 1)) + 
        (((17 * log(n) + 19) * ((n**3) + 2)))
        )
ftext = 'f(n) = (n^3 +n^2 log n)(log n +1) + (17 log n +19)(n^3 +2)'
cftext = 'C|f(n)|'

# Bounding function for f(x)
g = lambda n: (n**3) * log(n)
gtext = 'g(n) = %s'%title
cgtext = 'C|g(n)| = %d|%s|'%(C, title)

# Input size
size = 30

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

plt.plot(x, C*g_x, '--', color='green', label=cgtext, alpha=0.5)
#plt.plot(x, C*g_x, '--', color='green', label=cgtext, alpha=0.5)

#plt.plot(x, C*y, '--', color='blue', label=cftext, alpha=0.4)

plt.plot(w, vert, '--', label='k = %d'%k, color='grey', linewidth=1, alpha=0.4)
plt.title('f(n) is O(g(n)) (%s)'%name, loc='center')
plt.legend(loc=2)
plt.grid(linestyle=':', alpha=0.4)
plt.xlabel('Input')
plt.ylabel('Time')
plt.savefig(name+'_plot.jpg')
plt.show()
