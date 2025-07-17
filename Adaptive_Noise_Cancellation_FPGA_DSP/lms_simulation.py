import numpy as np
import matplotlib.pyplot as plt

def lms_filter(x, d, mu, N):
    w = np.zeros(N)
    y = np.zeros(len(x))
    e = np.zeros(len(x))

    for n in range(N, len(x)):
        x_n = x[n-N:n][::-1]
        y[n] = np.dot(w, x_n)
        e[n] = d[n] - y[n]
        w += 2 * mu * e[n] * x_n
    return y, e

# Simulated input signals
np.random.seed(0)
x = np.random.normal(0, 1, 500)
noise = 0.5 * np.random.normal(0, 1, 500)
d = x + noise

y, e = lms_filter(x, d, mu=0.01, N=8)

plt.plot(d, label="Noisy Signal")
plt.plot(e, label="Filtered Signal")
plt.legend()
plt.title("LMS Adaptive Filter")
plt.show()
