import board
import audiomp3
import audiobusio

audio = audiobusio.I2SOut(board.GP27, board.GP28, board.GP26)

mp3 = audiomp3.MP3Decoder(open("NeverGonnaGiveYouUp.mp3", "rb"))

audio.play(mp3)
while audio.playing:
    pass

print("Done playing!")
