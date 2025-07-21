import math, random
import numpy as np

n = 10000

def mountains(n):
    h = [0]*n
    for i in range(50):
        c = random.randint(20, n-20)
        w = random.randint(3, int(math.sqrt(n/5)))**2
        s = random.random()
        h[max(0, c-w):min(n, c+w)] = [h[i] + s*(w-abs(c-i)) for i in range(max(0, c-w), min(n, c+w))]

    low = min(h)
    high = max(h)
    h = [y - low for y in h]
    h = [y / (high - low) for y in h]
    return h

h = mountains(n)
x0 = random.randint(1, n-1)
x = x0
steps = 5000

def main(h, x):
    n = len(h)
    for step in range(steps):
        T = 2 * max(0, ((steps - step * 1.2) / steps))**3

        x_new = random.randint(max(0, x - 1000), min(n - 1, x + 1000))
        S_old = h[x]
        S_new = h[x_new]

        if S_new > S_old:
            x = x_new
        else:
            if T == 0:
                prob = 0
            else:
                prob = math.exp(-(S_old - S_new) / T)
            if random.random() < prob:
                x = x_new  # accept worse move probabilistically

    return x

x = main(h, x0)
print("ended up at %d, highest point is %d" % (x, np.argmax(h)))
