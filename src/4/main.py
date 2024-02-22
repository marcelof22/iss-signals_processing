# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

############################
# Projekt ISS              #
# Autor: Marcel Feiler     #
# Datum zacatia: 4.12.2021 #
############################

###################################
# 4. uloha - Spektrogram          #
###################################


def normal():
    import soundfile as sf
    from scipy.io import wavfile
    import matplotlib.pyplot as plt
    import numpy as np
    import IPython
    from scipy.signal import spectrogram, lfilter, freqz, tf2zpk
    import wavio

    data, fs = sf.read('../../audio/xfeile00.wav')
    f, t, sgr = spectrogram(data, fs, nperseg=1024, noverlap=512)
    spr_log = 10 * np.log10(sgr + 1e-20)

    plt.figure(figsize=(9, 6))
    plt.pcolormesh(t, f, spr_log)
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_ylabel('Frekvence [Hz]')
    cbar = plt.colorbar()
    cbar.set_label('Spektralní hustota výkonu [dB]', rotation=270, labelpad=15)

    plt.tight_layout()
    plt.show()
    plt.savefig('spectogram.pdf')



normal()
##################################################