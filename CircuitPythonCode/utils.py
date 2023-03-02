import os
import socketpool
import adafruit_requests
import wifi
import ipaddress
import ssl
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
endpointBase = str(os.getenv('API_ENDPOINT')) + "/"+str(os.getenv('HELMET_ID'))
endpointWholeState = endpointBase + ".json"
# https://learn.adafruit.com/adafruit-magtag/internet-connect
def getState():
    # Get the state from the remote json

    try:
        # print("fetching new state")
        response = requests.get(endpointWholeState) 
        myState = response.json()
    except Exception as e:
        print("Error getting json from", endpointWholeState, e)
        myState = {}
        pass    
    return myState

def setState(stateName, stateValue):
    data = {}
    data[stateName] = stateValue
    try:
        requests.patch(endpointWholeState , json=data)
    except Exception as e:
        print("Error setting state", e)
        pass
  

    