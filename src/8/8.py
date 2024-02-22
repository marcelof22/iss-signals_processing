############################
# Projekt ISS              #
# Autor: Marcel Feiler     #
# Datum zacatia: 4.12.2021 #
############################


#######################################
# 8. uloha - Nulove body a poly       #
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
    z, p, k = tf2zpk(b1, a1)
    ang = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.cos(ang), np.sin(ang))

    # nuly, poly
    plt.scatter(np.real(z), np.imag(z), marker='o', facecolors='none', edgecolors='r', label='nuly')
    plt.scatter(np.real(p), np.imag(p), marker='x', color='g', label='póly')

    plt.gca().set_title('Zobrazenie nulov a pólov navrhnutého filtra 1 $h[n]$')
    plt.gca().set_xlabel('Reálna zložka R{z}')
    plt.gca().set_ylabel('Imaginárna zložka I{z}')

    plt.grid(alpha=0.5, linestyle='--')
    plt.legend(loc='upper left')

    #plt.tight_layout()
    plt.savefig('1.pdf')
    plt.show()

    #############
    z, p, k = tf2zpk(b2, a2)
    ang = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.cos(ang), np.sin(ang))

    # nuly, poly
    plt.scatter(np.real(z), np.imag(z), marker='o', facecolors='none', edgecolors='r', label='nuly')
    plt.scatter(np.real(p), np.imag(p), marker='x', color='g', label='póly')

    plt.gca().set_title('Zobrazenie nulov a pólov navrhnutého filtra 2 $h[n]$')
    plt.gca().set_xlabel('Reálna zložka R{z}')
    plt.gca().set_ylabel('Imaginárna zložka I{z}')

    plt.grid(alpha=0.5, linestyle='--')
    plt.legend(loc='upper left')

    # plt.tight_layout()
    plt.savefig('2.pdf')
    plt.show()
    ###############
    z, p, k = tf2zpk(b3, a3)
    ang = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.cos(ang), np.sin(ang))

    # nuly, poly
    plt.scatter(np.real(z), np.imag(z), marker='o', facecolors='none', edgecolors='r', label='nuly')
    plt.scatter(np.real(p), np.imag(p), marker='x', color='g', label='póly')

    plt.gca().set_title('Zobrazenie nulov a pólov navrhnutého filtra 3 $h[n]$')
    plt.gca().set_xlabel('Reálna zložka R{z}')
    plt.gca().set_ylabel('Imaginárna zložka I{z}')

    plt.grid(alpha=0.5, linestyle='--')
    plt.legend(loc='upper left')

    # plt.tight_layout()
    plt.savefig('3.pdf')
    plt.show()
    ###############
    z, p, k = tf2zpk(b4, a4)
    ang = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.cos(ang), np.sin(ang))

    # nuly, poly
    plt.scatter(np.real(z), np.imag(z), marker='o', facecolors='none', edgecolors='r', label='nuly')
    plt.scatter(np.real(p), np.imag(p), marker='x', color='g', label='póly')

    plt.gca().set_title('Zobrazenie nulov a pólov navrhnutého filtra 4 $h[n]$')
    plt.gca().set_xlabel('Reálna zložka R{z}')
    plt.gca().set_ylabel('Imaginárna zložka I{z}')

    plt.grid(alpha=0.5, linestyle='--')
    plt.legend(loc='upper left')

    # plt.tight_layout()
    plt.savefig('4.pdf')
    plt.show()

normal()