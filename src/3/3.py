############################
# Projekt ISS              #
# Autor: Marcel Feiler     #
# Datum zacatia: 4.12.2021 #
############################

#######################################
# 3. uloha - DFT                      #
#######################################

def normal():
    import soundfile as sf
    from scipy.io import wavfile
    import matplotlib.pyplot as plt
    import numpy as np
    import IPython
    from scipy.signal import spectrogram, lfilter, freqz, tf2zpk
    import wavio

    fs, data = wavfile.read('../../audio/xfeile00.wav')

    data_abs = abs(data.max())
    data = data - np.mean(data)
    data = data / data_abs
    data = data.T
    data_length = len(data)

    frames = []
    position = 0

    for i in range(data_length // 512):
        frame = data[position:position+1024]
        frames.append(frame)
        position += 512

    t = np.arange(1024) / fs

    N = 1024
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)

    X = np.dot(e, frames[8])

    plt.figure(figsize=(6, 5))
    plt.title('DFT')
    plt.gca().set_xlabel('$f[Hz]$')
    plt.plot(np.arange(0, fs / 2, fs / 2 / 512), np.abs(X[:512]))
    plt.savefig('DFT.pdf')

normal()

