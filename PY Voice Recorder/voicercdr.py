#  pip install sounddevice ,  scipy
import sounddevice as sdv
from scipy.io.wavfile import write

# This will work with devices having an audio input

scnds = int(input("Required seconds of audio you want to record - "))
print("Recording started......")
rcrdn = sdv.rec((scnds*44100), channels=2)
sdv.wait()

fl_name = input("Give the audio file a name - ")
write(fl_name, 44100, rcrdn)
print("Recording is done.....")
