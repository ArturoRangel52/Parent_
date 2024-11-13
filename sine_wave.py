import matplotlib.pyplot as plt
import numpy as np

Fs = 8000
f = 3 #frequency
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, y)
plt.show()

#modified and copied from
#https://stackoverflow.com/questions/22566692/how-to-plot-graph-sine-wave#:~:text=A%20simple%20way%20to%20plot%20sine%20wave%20in,as%20plt%20x%3Dnp.arange%280%2C3%2Anp.pi%2C0.1%29%20y%3Dnp.sin%28x%29%20plt.plot%28x%2Cy%29%20plt.title%28%22SINE%20WAVE%22%29%20plt.show%28%29