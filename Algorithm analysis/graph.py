import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 1000)
m = np.arange(1, 31)

plt.figure(figsize=(10, 6))

# set new range m, because 2^1000 is to big to show
plt.plot(n, np.log(n), label="$\log_{2} n$")  # 수의 subscribt를 나타내는 LaTeX
plt.plot(n, n, label="n")
plt.plot(n, n*np.log(n), label="$n \log_{2} n$")
plt.plot(n, n**2, label="n**2")
plt.plot(n, n**3, label="n**3")
plt.plot(m, 2**m, label="2**m")


# for better looking graph
plt.xscale("log")
plt.yscale("log")
plt.xlim(3, 1000)
plt.ylim(1, 1000000)
plt.xlabel("size")
plt.ylabel("time")

# show legend and grid
plt.legend(loc="upper left")
plt.grid(True)

plt.show()
