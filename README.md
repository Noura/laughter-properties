# How to use

## First time setup

From the command line:

```
  git clone --recursive https://github.com/Noura/laughter-properties
  cd laughter-properties
  touch laughter_detection/__init__.py
```

Make sure all the audio files you want to process are in .wav format. If needed you can convert them with VLC, which you can download for free from <a href="http://download.cnet.com/VLC-Media-Player-64-bit/3000-13632_4-75761094.html">here</a>.

## Every time usage

### Convert files to .wav format

Make sure all the audio files to .wav format. If needed you can conver them with VLC.

Launch VLC, go to `File -> Convert/Stream`.

Add the audio file you want to convert.

Under `Choose Profile`, choose wav. 

<strong>If wav file format is not an option for you... </strong> If wav is not an option, click `Customize...` then on the `Encapsulation` tab choose `WAV`, on the `Audio codec` tab choose `WAV`, then click `Save as new Profile...` and name it `my wav` or something descriptive. You should only need to do this the first time you Convert/Stream with VLC, in the future you can just make sure to choose the `my wav` profile.

Choose an output destination and name for the .wav file.

### Organize the files

Put all the .wav files that you want to have processed together in the same folder. We'll refer to this folder as `input_directory`

### Run the script

Launch a terminal session in the folder `laughter-properties`

From the command line:

```
  python process_laughs.py <input_directory>
```

Where `input_directory` is the absolute path of the folder containing the .wav files

### View the results

Navigate to `input_directory` and open `results.txt`

"relative loudness" is roughly the loudness of the laughter snippet divided by the average loudness of the whole audio recording. So, this tries to take care of the differences in overall loudness of different audio recordings.


