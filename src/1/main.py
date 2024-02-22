# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

############################
# Projekt ISS              #
# Autor: Marcel Feiler     #
# Datum zacatia: 4.12.2021 #
############################

###########################
# 1. uloha - Zaklady      #
###########################


def normal():
    import soundfile as sf
    from scipy.io import wavfile
    import matplotlib.pyplot as plt
    import numpy as np
    import IPython
    from scipy.signal import spectrogram, lfilter, freqz, tf2zpk
    import wavio

    data, fs = sf.read('../../audio/xfeile00.wav')
    data = data[:250000]
    data.min(), data.max()

    data_length = len(data)
    print("Dlzka signalu vo vzorkoch:", data_length)
    print("Dlzka signalu v sekundach [s]", data_length / fs)

    print("Data min:", data.min())
    print("Data max:", data.max())

    t = np.arange(data.size) / fs
    plt.figure(figsize=(6, 3))
    plt.plot(t, data)

    plt.gca().set_xlabel('$t[s]$')
    plt.gca().set_title('Zvukový signál')
    plt.tight_layout()
    IPython.display.display(IPython.display.Audio(data, rate=fs))
    plt.savefig('test.pdf')
    # wavio - potreba normalizace
   # plt.figure()
   # plt.plot(np.arange(100), np.arange(100))

normal()
##################################################