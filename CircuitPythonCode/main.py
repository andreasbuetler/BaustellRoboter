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
while notConnected or attempts == 10:
    try:
        wifi.radio.connect(wifiSSID, wifiPassword)
        notConnected = False
    except:
        attempts += 1
        print("Connection failed on attempt %d" % attempts)
        pass
print("Connected to WiFi")
# https://learn.adafruit.com/adafruit-magtag/internet-connect
# pool = socketpool.SocketPool(wifi.radio)
# requests = adafruit_requests.Session(pool, ssl.create_default_context())
# endpoint = os.getenv('API_ENDPOINT')
# print("Fetching json from", endpoint)
# response = requests.get(endpoint)
# stateOfAll = response.json()["helmetStates"]
# myState = stateOfAll[os.getenv("HELMET_ID")]
# print("-" * 40)
# print()
# print("-" * 40)


audio = audiobusio.I2SOut(board.GP27, board.GP28, board.GP26)
# ngyu = audiomp3.MP3Decoder(open("NeverGonnaGiveYouUp.mp3", "rb"))
slow = audiomp3.MP3Decoder(open("slow.mp3", "rb"))

myState = utils.getState()
while True:
    newState = utils.getState()
    if newState["shouldPlay"] != myState["shouldPlay"]:
        if newState["shouldPlay"]:
            audio.play(slow)
        else:
            audio.stop()
    myState = newState
    time.sleep(1)
    pass

print("Done playing!")
