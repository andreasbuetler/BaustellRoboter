import os
import time
import board
import audiomp3
import audiobusio
import motor


audio = audiobusio.I2SOut(board.GP27, board.GP28, board.GP26)
ngyu = audiomp3.MP3Decoder(open("NeverGonnaGiveYouUp.mp3", "rb"))
audio.play(ngyu)
while audio.playing:
    motor.forwards()
    pass

print("Done playing!")
