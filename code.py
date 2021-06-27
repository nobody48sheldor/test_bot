import matplotlib.pyplot as plt
import numpy as np
from math import *
import time

result = []

n = 200

x = np.linspace(0, 10, n)

def func(x):
    s = np.exp(-0.01*x**2)*np.sin(x)
    return(s)

y = func(x)

plt.plot(x, y)
plt.savefig('result')

result.append(n)

with open("results.txt", 'w') as file:
    for i in range(len(result)):
        file.write("{}".format(result[i]))

with open("run.txt", "w+") as file_start:
    file_start.write("done")

time.sleep(2)

with open("run.txt", "w+") as file_start:
    file_start.write("nope")
