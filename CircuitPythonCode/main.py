import os
import time
import board
import audiomp3
import audiobusio
import motor
# wifi stuff
import wifi
import socketpool
import ipaddress
import adafruit_requests
import ssl
import utils
# Connect ot WIFI
print("Available WiFi networks:")
for network in wifi.radio.start_scanning_networks():
    print("\t%s\t\tRSSI: %d\tChannel: %d" % (str(network.ssid, "utf-8"),
            network.rssi, network.channel))
wifi.radio.stop_scanning_networks()
wifiSSID = os.getenv('WIFI_SSID')
print("Connecting to %s" % wifiSSID)
wifiPassword = os.getenv('WIFI_PASSWORD')
print("Password: %s" % wifiPassword)
notConnected = True
attempts = 0
while notConnected and attempts <= 10:
    try:
        wifi.radio.connect(wifiSSID, wifiPassword)
        notConnected = False
        print("Connected to WiFi")
    except:
        attempts += 1
        print("Connection failed on attempt %d" % attempts)
        pass



audio = audiobusio.I2SOut(board.GP27, board.GP28, board.GP26)
# ngyu = audiomp3.MP3Decoder(open("NeverGonnaGiveYouUp.mp3", "rb"))
# array of audio files
allAudioFiles = []
for i in range(0, 10):
    indexString = str(i)
    try:
        audioFileDecoded = audiomp3.MP3Decoder(open(indexString + ".mp3", "rb"))
        allAudioFiles.append(audioFileDecoded)
    except:
        print("No file named", indexString + ".mp3")
        pass

myState = utils.getState()
# todo hanlde case where there is connection
while True:
    newState = utils.getState()
    if newState["shouldPlay"]:
        
        try:
            audioToPlay = allAudioFiles[int(newState["audio"])]
            print("Playing audio", newState["audio"], ".mp3")
            audio.play(audioToPlay)
            utils.setState("shouldPlay", False)
        except:
            print("No audio file with index", newState["audio"])
            pass
     
    while audio.playing:
        time.sleep(.1)
    pass

print("Done playing!")
