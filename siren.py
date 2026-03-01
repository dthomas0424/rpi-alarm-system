import time
import soundfile as sf
import soundcard as sc

default_speaker = sc.default_speaker()
samples, samplerate = sf.read('your_soundfile_here')

default_speaker.play(samples, samplerate=samplerate)

time.sleep(0.1)

default_speaker.play(samples, samplerate=samplerate)
