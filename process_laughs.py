import laughter_detection.segment_laughter as segment
import json
import librosa
import numpy
import os
import sys

##############################################
# SETTINGS ###################################
# You can tweak these values to adjust the laughter detection performance

# The threshold parameter adjusts the minimum probability threshold for classifying a frame as laughter. The default is 0.5, but you can  experiment with settings between 0 and 1 to see what works best for your data. Lower threshold values may give more false positives but may also recover a higher percentage of laughs from your file. (quoted from detection/README.md)
threshold = 0.5

# The min_length parameter sets the minimum length in seconds that a laugh needs to be in order to be identified. The default value is 0.2. (quoted from detection/README.md)
min_length = 0.2

# The machine learning model that will be used to detect laughter
model = 'laughter_detection/models/new_model.h5'

# Name of the file where the results will be saved
results_filename = "results.txt"
##############################################

def analyze_recording(src):
    output_dir = src.strip('.wav')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
            
    laughs = segment.laugh_segmenter.segment_laughs(src, model, output_dir, threshold, min_length)

    # loudness of audio
    def loudness(a):
        y, sr = librosa.load(a)
        rms = librosa.feature.rmse(y=y)
        # average and make it a native Python float instead of numpy float type
        avg_rms = numpy.mean(rms).item()
        return avg_rms

    base_loudness = loudness(src)

    for l in laughs:
        # lengh (duration in seconds) of each laugh
        l['length'] = l['end'] - l['start']
        # loudness of each laugh
        l['relative loudness'] = loudness(l['filename'])/base_loudness

    res= {}
    res['source file'] = src
    res['output directory'] = output_dir
    res['detected laughs'] = laughs
    res['total number of laughs detected'] = len(laughs)
    return res


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Error: Please provide the directory path where the audio files (in .wav format) are located.")

    input_dir = sys.argv[1]

    if not os.path.exists(input_dir):
        sys.exit("Error: The path " + input_dir + " was not found. Please check the path and try again.")

    report = {}
    for f in os.listdir(input_dir):
        if f.endswith('.wav'):
            fullpath = os.path.join(input_dir, f)
            print "\n\n\n*******************************************\nprocessing file", fullpath
            d = analyze_recording(fullpath)
            report[fullpath] = d

    with open(os.path.join(input_dir, results_filename), 'w') as f:
        json.dump(report, f, sort_keys=True, indent=4)
