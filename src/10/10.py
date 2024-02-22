############################
# Projekt ISS              #
# Autor: Marcel Feiler     #
# Datum zacatia: 4.12.2021 #
############################


#######################################
#10. uloha - Filtrace                 #
#######################################

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
    fil = lfilter(b1, a1, data)
    fil = lfilter(b2, a2, fil)
    fil = lfilter(b3, a3, fil)
    fil = lfilter(b4, a4, fil)

    f, t, sfgr = spectrogram(fil, fs)
    sfgr_log = 10 * np.log10(sfgr + 1e-20)

    plt.figure(figsize=(9, 3))
    plt.pcolormesh(t, f, sfgr_log)
    plt.gca().set_title('Spektrum vyfiltrovaného signálu')
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_ylabel('Frekvencia [Hz]')
    cbar = plt.colorbar()
    cbar.set_label('Spektrálna hustota výkonu [dB]', rotation=270, labelpad=15)

    plt.tight_layout()



    sf.write('../../audio/clean_bandstop.wav', fil, fs)

    #plt.tight_layout()
    plt.savefig('Spektrum_vyf_sig.pdf')

    ##
"""
    N_imp = 19
    imp = [1, *np.zeros(N_imp - 1)]  # jednotkovy impuls
    h = lfilter(bk, ak, imp)

    plt.figure(figsize=(5, 3))
    plt.stem(np.arange(N_imp), h, basefmt=' ')
    plt.gca().set_xlabel('$n$')
    plt.gca().set_title('Impulsní odezva $h[n]$')

    plt.grid(alpha=0.5, linestyle='--')

    plt.tight_layout()
    plt.show()
    plt.savefig('impodozva.pdf')
"""


normal()