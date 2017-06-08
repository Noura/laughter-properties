import sox


def mean_freq(a_file):
    tfm = sox.Transformer()
    dft = tfm.power_spectrum(a_file)
    mean = sum([x[0] * x[1] for x in dft]) / sum([x[1] for x in dft])
    return mean


