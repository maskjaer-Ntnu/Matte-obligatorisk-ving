import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 30, 300)

def f(x):
    return 19.5 + 15*2.71**(-0.0202*x)

plt.plot(x, f(x), label = 'Diff likning', color = 'red')

data = [34.5, 34.2, 33.7, 33.3, 32.9, 32.4, 32.1, 31.6, 31.3, 30.9, 30.6, 30.3, 29.9, 
        29.6, 29.3, 29.0, 28.8, 28.4, 28.1, 27.9, 27.7, 27.4, 27.2, 27.0, 26.9, 26.6, 26.4, 26.2, 26.0, 25.8, 25.7]

tid = list(range(len(data)))

plt.plot(tid, data, label = 'målt data', color = 'blue')

plt.legend()
plt.grid()
plt.xlabel('tid')
plt.ylabel('temperatur')
plt.show()
