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


myState = utils.getState()
# todo hanlde case where there is connection
progressInCurrentAction = 0
while True:
    newState = utils.getState()
    if newState:
        # if we have an audio override play it and then set the state shouldPlay to false
        if newState["audioOverride"] and newState["audioOverride"]["shouldPlay"]:
            audioFileIndex = newState["audioOverride"]["audioFileIndex"]
            utils.playAudioFile(audioFileIndex)
            utils.setState("shouldPlay", False, "/audioOverride")
        
        actionIndex = newState["actionIndex"]
        # access an action with the actionIndex
        if newState["actionIndex"] >=0 and newState["actions"]:
            actionsArray = newState["actions"]
            currentAction = actionsArray[actionIndex]
            newActionIndex = (actionIndex + 1) % len(actionsArray)
            # if we have not completed the current action
            if currentAction["type"] == "sound":
                utils.playAudioFile(currentAction["audioFileIndex"])
                utils.setState("actionIndex", newActionIndex)
            elif progressInCurrentAction < currentAction["length"]:
                if currentAction["type"] == "drive":
                    direction = currentAction["direction"]
                    progressInCurrentAction += 1
                    if direction == "forwards":
                        motor.forwards()
                    elif direction == "backwards":
                        motor.backwards()
                    elif direction == "turnLeft":
                        motor.turnLeft()
                    elif direction == "turnRight":
                        motor.turnRight()
                    elif direction == "stop":
                        motor.stop()
            # if we have completed the current action set the actionIndex to the next action
            else:
                progressInCurrentAction = 0
                utils.setState("actionIndex", newActionIndex)

print("Done playing!")
