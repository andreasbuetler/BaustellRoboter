import os
import socketpool
import adafruit_requests
import wifi
import ssl
import audiomp3
import audiobusio
import board
import time
# https://learn.adafruit.com/adafruit-magtag/internet-connect
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
endpointBase = str(os.getenv('API_ENDPOINT')) + "/"+str(os.getenv('HELMET_ID'))
endpointWholeState = endpointBase + ".json"
# audio setup
audio = audiobusio.I2SOut(board.GP27, board.GP28, board.GP26)
print("audio setup")
def getState()->dict:
    # Get the state from the remote json
    try:
        # print("fetching new state")
        response = requests.get(endpointWholeState) 
        myState = response.json()
    except Exception as e:
        print("Error getting json", e )
        myState = {}
        pass    
    return myState

def setState(stateName, stateValue, statePath=""):
    data = {}
    data[stateName] = stateValue
    try:
        requests.patch(endpointBase + statePath + ".json" , json=data)
    except Exception as e:
        print("Error setting state", e)
        pass
  

def playAudioFile(audioFileIndex: int, audioOutput) -> bool:
    # play the audio file
    if audioOutput is None:
        print("audio is none")
        audioOutput = audiobusio.I2SOut(board.GP27, board.GP28, board.GP26)
    indexString = str(audioFileIndex)
    try:
        audioFile = open("Audio/" + indexString + ".mp3", "rb")
        audioFileDecoded = audiomp3.MP3Decoder(audioFile)
        print("Playing audio", indexString)
        audioOutput.play(audioFileDecoded)
        while audioOutput.playing:
            time.sleep(0.1)
        del audioFileDecoded
        del audioFile
        return True
    except:
        print("Could not play audio:", indexString)
        return False
        pass