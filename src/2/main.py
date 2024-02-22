# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

############################
# Projekt ISS              #
# Autor: Marcel Feiler     #
# Datum zacatia: 4.12.2021 #
############################

#######################################
# 2. uloha - Predspracovani a ramce   #
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

    plt.figure(figsize=(6, 5))
    plt.title('Ramec s periodickym znelym charakterom')
    plt.gca().set_xlabel('$t[s]$')
    plt.plot(t, frames[28])
    plt.savefig('28 ramec.pdf')


normal()
##################################################