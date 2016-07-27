import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.io import wavfile

sigrate, sig = wavfile.read('voice.wav')
print(sigrate, len(sig))

widths = np.arange(1, 1001)

cwtmatr = signal.cwt(sig, signal.ricker, widths)
plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
plt.show()
