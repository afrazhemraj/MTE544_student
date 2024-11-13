import math
parabola = []
for i in range(0,16):
    x = i/10
    y = x**2
    parabola.append([x,y])

sigmoid = []
for i in range(0,26):
    x = i/10
    y = 2/(1+ math.exp(-2*x)) - 1
    sigmoid.append([x,y])