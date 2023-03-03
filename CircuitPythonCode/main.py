import os
import time
import board

import audiobusio
import motor
# wifi stuff
import wifi
import utils
import gc

def main():
    # Connect ot WIFI
    # print("Available WiFi networks:")
    # for network in wifi.radio.start_scanning_networks():
    #     print("\t%s\t\tRSSI: %d\tChannel: %d" % (str(network.ssid, "utf-8"),
    #             network.rssi, network.channel))
    # wifi.radio.stop_scanning_networks()
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
    # audio setup
    audioOutput = audiobusio.I2SOut(board.GP27, board.GP28, board.GP26)

    # todo hanlde case where there is connection
    timestamp = -1
    oldActionIndex = None
    while True:
        newState = utils.getState()
        # print("memory free:", gc.mem_free())
        if newState:
            # if we have a new state
            if oldActionIndex != newState["actionIndex"]:
                # if we have a new state set the timestamp to the current time
                print("new state")
                timestamp = time.monotonic()
                oldActionIndex = newState["actionIndex"]
            # if we have an audio override play it and then set the state shouldPlay to false
            if newState["audioOverride"] and newState["audioOverride"]["shouldPlay"]:
                audioFileIndex = newState["audioOverride"]["audioFileIndex"]
                didPlay = utils.playAudioFile(audioFileIndex, audioOutput)
                utils.setState("shouldPlay", not didPlay, "/audioOverride")
                del audioFileIndex
            
            actionIndex = newState["actionIndex"]
            # access an action with the actionIndex
            if newState["actionIndex"] >=0 and newState["actions"]:
                # print("progressInCurrentAction",progressInCurrentAction)
                actionsArray = newState["actions"]
                currentAction = actionsArray[actionIndex]
                newActionIndex = (actionIndex + 1) % len(actionsArray)
                del actionsArray
                # if we have not completed the current action
                if currentAction["type"] == "sound":
                    utils.playAudioFile(currentAction["audioFileIndex"], audioOutput)
                    utils.setState("actionIndex", newActionIndex)
                elif time.monotonic() <= currentAction["length"] + timestamp:
                    if currentAction["type"] == "drive":
                        direction = currentAction["direction"]
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
                    del currentAction
                # if we have completed the current action set the actionIndex to the next action
                else:
                    utils.setState("actionIndex", newActionIndex)
while True:
    try:
        main()
    except Exception as e:
        print("Error in main", e)
        pass