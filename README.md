# audioslice auto slice audio into 1000ms 

# usage
``` python
python SliceAudio.py  -I "./data/"  -O  "./output/"

```
Dependencies:
1. gcc
2. pydub (sudo pip install pydub), see https://github.com/jiaaro/pydub
3. ffmpeg (brew install libav --with-libvorbis --with-sdl --with-theora)
4. audioread (sudo pip install audioread)
Default will spit out wav file slices of 2 second duration, in 16bit/mono/44.1kHz sample rate (Useful for the
Analog Elektron Rytm drum machine).
Will chop up the input file and spit out slices along its length until it reaches the end of the file.
Can input/output in any format that ffmpeg supports.
example usage:
python SliceAudio.py -i xyz.m4a -f m4a -b 2 -s 11025 -l 10000
python SliceAudio.py -h

To do:
~~    add support to set output destination folder ~~

	add support to only output glued reversed chunks (i.e., turn off full output)

	allow naming of glued reverse-granule file



