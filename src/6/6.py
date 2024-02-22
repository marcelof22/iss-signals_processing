############################
# Projekt ISS              #
# Autor: Marcel Feiler     #
# Datum zacatia: 4.12.2021 #
############################

#######################################
# 6. uloha - Generování signálu       #
#######################################

def normal():
    import soundfile as sf
    from scipy.io import wavfile
    import matplotlib.pyplot as plt
    import numpy as np
    import IPython
    from scipy.signal import spectrogram, lfilter, freqz, tf2zpk
    import wavio

    data, fs = sf.read('../../audio/xfeile00.wav')
    lendata = len(data)

    fq1 = 670
    fq2 = 1360
    fq3 = 2030
    fq4 = 2700

    vzorka = []
    for i in range(lendata):
        vzorka.append(i/fs)

    _1out_cos = np.cos(2*np.pi*fq1*np.array(vzorka))
    _2out_cos = np.cos(2*np.pi*fq2*np.array(vzorka))
    _3out_cos = np.cos(2*np.pi*fq3*np.array(vzorka))
    _4out_cos = np.cos(2*np.pi*fq4*np.array(vzorka))

    out_cos = _1out_cos+_2out_cos+_3out_cos+_4out_cos

    sf.write("../../audio/4cos.wav", out_cos, fs)
###
    #data1, fs1 = sf.read('prefinal.wav')
    f, t, sgr = spectrogram(out_cos, fs, nperseg=1024, noverlap=512)
    spr_log = 10 * np.log10(sgr + 1e-20)

    plt.figure(figsize=(9, 3))
    plt.pcolormesh(t, f, spr_log)
    plt.gca().set_xlabel('Čas [s]')
    plt.gca().set_ylabel('Frekvence [Hz]')
    cbar = plt.colorbar()
    cbar.set_label('Spektralní hustota výkonu [dB]', rotation=270, labelpad=15)

    plt.tight_layout()
    #plt.show()
    plt.savefig('test.pdf')

normal()