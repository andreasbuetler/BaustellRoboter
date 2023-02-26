print('hello')
# """
# CircuitPython I2S MP3 playback example.
# Plays a single MP3 once.
# """
# import audiomp3
# import audiobusio

# # bit clock = GP27
# # Word clock = GP28
# # Data = GP26
# audio = audiobusio.I2SOut(27, 28, 26)

# mp3 = audiomp3.MP3Decoder(open("Audio/TestAudioLQ.mp3", "rb"))

# audio.play(mp3)
# while audio.playing:
#     pass



import machine
import uwave

# Configure I2S interface
i2s = machine.I2S(sck=machine.Pin(27), ws=machine.Pin(28), sd=machine.Pin(26))
i2s.init(i2s.MASTER, i2s.TX, sample_rate=44100, bits=16, channels=2, dma=1)


# Open WAV file and read data into buffer
with open('audio.wav', 'rb') as f:
    wave_reader = uwave.Wave_read(f)
    data = bytearray(wave_reader.readframes(wave_reader.getnframes()))

# Write audio data to I2S interface
i2s.write(data)
print("Done playing!")