import os
import sox
import librosa
import matplotlib.pyplot as plt

def mean_hz(a_file):
    tfm = sox.Transformer()
    dft = tfm.power_spectrum(a_file)
    mean = sum([x[0] * x[1] for x in dft]) / sum([x[1] for x in dft])
    return mean

def peak_hz(a_file):
    tfm = sox.Transformer()
    dft = tfm.power_spectrum(a_file)
    max_amp = 0
    for i in range(0, len(dft)):
        if (dft[i][1] > max_amp):
            max_amp = dft[i][1]
            max_hz = dft[i][0]
    return max_hz

def tempo(a_file):
    y, sr = librosa.load(a_file)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return tempo


def test_plot(func, src):
    y = []
    labels = [f for f in os.listdir(src) if f.endswith('.wav')]
    x = range(0, len(labels))
    for filename in labels:
        y.append(func(src+filename))
    plt.plot(y, 'g^')
    plt.xticks(x, labels, rotation='vertical')
    plt.ylabel(func.__name__)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':

    src = '../laughter-samples/test/'

    test_plot(peak_hz, src)
