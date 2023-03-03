import os
import socketpool
import adafruit_requests
import wifi
import ipaddress
import ssl
import audiomp3
import audiobusio
import board
# https://learn.adafruit.com/adafruit-magtag/internet-connect
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
endpointBase = str(os.getenv('API_ENDPOINT')) + "/"+str(os.getenv('HELMET_ID'))
endpointWholeState = endpointBase + ".json"
# audio setup
audio = audiobusio.I2SOut(board.GP27, board.GP28, board.GP26)

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
  

def playAudioFile(audioFileIndex: int):
    # play the audio file
    indexString = str(audioFileIndex)
    try:
        audioFile = open("Audio/" + indexString + ".mp3", "rb")
        audioFileDecoded = audiomp3.MP3Decoder(audioFile)
        print("Playing audio", indexString, ".mp3")
        audio.play(audioFileDecoded)
        
    except:
        print("No audio file with index", indexString)
        pass