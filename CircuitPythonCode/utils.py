import os
import socketpool
import adafruit_requests
import wifi
import ssl
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
endpoint = str(os.getenv('API_ENDPOINT')) + str(os.getenv('HELMET_ID')) + ".json"
def getState():
    # Get the state from the remote json
    print("Fetching json from", endpoint)
    response = requests.get(endpoint) 
    stateOfAll = response.json()["helmetStates"]
    myState = stateOfAll[os.getenv("HELMET_ID")]
    print(myState)

    return myState