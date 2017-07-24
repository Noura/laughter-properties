# How to use

## First time setup - get the code

From the command line:

```
  git clone --recursive https://github.com/Noura/laughter-properties
  cd laughter-properties
  touch laughter_detection/__init__.py
  touch pywebrtcvad/__init__.py
```

## First time setup - Set up VLC to convert to WAV
You need to make sure all the audio files you want to process are in .wav format, mono, sample rate at 8000, 16000, or 32000, and sample width 2. If you need to convert the audio files to this format, you can use VLC, which you can download for free from <a href="http://download.cnet.com/VLC-Media-Player-64-bit/3000-13632_4-75761094.html">here</a>.

In VLC, go to `File -> Convert/Stream`

Under `Choose Profile`, choose `Custom` from the dropdown then press the button `Customize...`

In the popup menu,
under `Encapsulation` choose `WAV`
under `Audio codec` choose `Codec: WAV`, `Channels: 1`, `Samplerate: 8000`

Click `Save as new Profile...`, I suggest naming it something descriptive like `wav mono sr8000`.

Now every time you want to convert a file you can choose this profile.

## Every time usage

### Convert files to .wav format

Make sure all the audio files to .wav format. If needed you can conver them with VLC.

Launch VLC, go to `File -> Convert/Stream`.

Add the audio file you want to convert.

Under `Choose Profile`, choose `wav mono sr8000` or whatever you named your custom profile. 

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


