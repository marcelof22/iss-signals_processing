############################
# Projekt ISS              #
# Autor: Marcel Feiler     #
# Datum zacatia: 4.12.2021 #
############################


########################################
#9. uloha - Frekvencni charakteristika #
########################################

def normal():
    import soundfile as sf
    from scipy.io import wavfile
    import matplotlib.pyplot as plt
    import numpy as np
    import IPython
    from scipy.signal import spectrogram, lfilter, freqz, tf2zpk
    import wavio
    from scipy import signal

    data, fs = sf.read('../../audio/xfeile00.wav')

    f1 = 670
    f2 = 1360
    f3 = 2030
    f4 = 2700

    spread1 = 80
    spread2 = 30
    bpass = 3
    bstop = 40

    n, wn = signal.buttord([(f1-spread1)/(fs/2), (f1+spread1)/(fs/2)], [(f1-spread2)/(fs/2), (f1+spread2)/(fs/2)], bpass, bstop)
    b1, a1 = signal.butter(n, wn, 'bandstop')

    n, wn = signal.buttord([(f2 - spread1) / (fs / 2), (f2 + spread1) / (fs / 2)], [(f2 - spread2) / (fs / 2), (f2 + spread2) / (fs / 2)], bpass, bstop)
    b2, a2 = signal.butter(n, wn, 'bandstop')

    n, wn = signal.buttord([(f3 - spread1) / (fs / 2), (f3 + spread1) / (fs / 2)], [(f3 - spread2) / (fs / 2), (f3 + spread2) / (fs / 2)], bpass, bstop)
    b3, a3 = signal.butter(n, wn, 'bandstop')

    n, wn = signal.buttord([(f4 - spread1) / (fs / 2), (f4 + spread1) / (fs / 2)], [(f4 - spread2) / (fs / 2), (f4 + spread2) / (fs / 2)], bpass, bstop)
    b4, a4 = signal.butter(n, wn, 'bandstop')

    ak = np.convolve(np.convolve(np.convolve(a1, a2), a3), a4)
    bk = np.convolve(np.convolve(np.convolve(b1, b2), b3), b4)
    ##
    width1, height1 = signal.freqz(b1, a1)
    width2, height2 = signal.freqz(b2, a2)
    width3, height3 = signal.freqz(b3, a3)
    width4, height4 = signal.freqz(b4, a4)

    plt.figure()
    plt.plot(width1 / 2 / np.pi * fs, 20 * np.log10(abs(height1)))
    plt.plot(width2 / 2 / np.pi * fs, 20 * np.log10(abs(height2)))
    plt.plot(width3 / 2 / np.pi * fs, 20 * np.log10(abs(height3)))
    plt.plot(width4 / 2 / np.pi * fs, 20 * np.log10(abs(height4)))
    plt.gca().set_title('Frekvenčná odozva navrhnutého filtra $h[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.grid(alpha=0.5, linestyle='--')
    plt.savefig('fr_response.png')
    plt.show()



    #########################################

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(width1 / 2 / np.pi * fs, np.abs(height1))
    plt.gca().set_title('Modul frekvenčnej charakteristiky $|H(e^{j\omega})|$ filtru $h_1[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.grid(alpha=0.5, linestyle='--')
    plt.subplot(2, 1, 2)
    plt.plot(width1 / 2 / np.pi * fs, np.angle(height1))
    plt.gca().set_title('Argument frekvenčnej charakteristiky arg $H(e^{j\omega})$ filtru $h_1[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.savefig('fr1.png')
    plt.grid(alpha=0.5, linestyle='--')
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(width2 / 2 / np.pi * fs, np.abs(height2))
    plt.gca().set_title('Modul frekvenčnej charakteristiky $|H(e^{j\omega})|$ filtru $h_2[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.grid(alpha=0.5, linestyle='--')
    plt.subplot(2, 1, 2)
    plt.plot(width2 / 2 / np.pi * fs, np.angle(height2))
    plt.gca().set_title('Argument frekvenčnej charakteristiky arg $H(e^{j\omega})$ filtru $h_2[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.savefig('fr2.png')
    plt.grid(alpha=0.5, linestyle='--')
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(width3 / 2 / np.pi * fs, np.abs(height3))
    plt.gca().set_title('Modul frekvenčnej charakteristiky $|H(e^{j\omega})|$ filtru $h_3[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.grid(alpha=0.5, linestyle='--')
    plt.subplot(2, 1, 2)
    plt.plot(width3 / 2 / np.pi * fs, np.angle(height3))
    plt.gca().set_title('Argument frekvenčnej charakteristiky arg $H(e^{j\omega})$ filtru $h_3[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.savefig('fr3.png')
    plt.grid(alpha=0.5, linestyle='--')
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(width4 / 2 / np.pi * fs, np.abs(height4))
    plt.gca().set_title('Modul frekvenčnej charakteristiky $|H(e^{j\omega})|$ filtru $h_4[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.grid(alpha=0.5, linestyle='--')
    plt.subplot(2, 1, 2)
    plt.plot(width4 / 2 / np.pi * fs, np.angle(height4))
    plt.gca().set_title('Argument frekvenčnej charakteristiky arg $H(e^{j\omega})$ filtru $h_4[n]$')
    plt.gca().set_xlabel('Frekvencia [Hz]')
    plt.savefig('fr4.png')
    plt.grid(alpha=0.5, linestyle='--')
    plt.tight_layout()
    plt.show()


normal()