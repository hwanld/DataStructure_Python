from time import time
import matplotlib.pyplot as plt
import numpy as np

import prefixAverage

sz = 1000

# Generate random sample of size
S = np.random.randint(low=1, high=100, size=1000)
T = np.arange(sz)

A = prefixAverage.prefix_average1(S)
Tx1 = [0]*sz
Tx2 = [0]*sz
Tx3 = [0]*sz

for i in range(sz):
    temp = np.random.randint(low=1, high=100, size=i)
    starttime = time()
    prefixAverage.prefix_average1(temp)
    endtime = time()
    Tx1[i] = (endtime-starttime)*1000
    starttime = time()
    prefixAverage.prefix_average2(temp)
    endtime = time()
    Tx2[i] = (endtime-starttime)*1000
    starttime = time()
    prefixAverage.prefix_average3(temp)
    endtime = time()
    Tx3[i] = (endtime-starttime)*1000


plt.figure(figsize=(10, 6))

plt.plot(T, Tx1, label="prefix_average1")
plt.plot(T, Tx2, label="prefix_average2")
plt.plot(T, Tx3, label="prefix_average3")

plt.xscale("log")
plt.yscale("log ")
plt.xlim(100, 1000)
plt.ylim(0, 100)
plt.xlabel("size")
plt.ylabel("time")

# show legend and grid
plt.legend(loc="upper left")
plt.grid(True)

plt.show()
