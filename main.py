
import json
import requests
import time

# Import based on using a physical RPi or the emulator
#from sense_emu import SenseHat
from sense_emu import SenseHat

# Constants
INTERVAL            = 3  #Data capture and upload interval in seconds.
API_KEY             = "qdw0aq16tr2ejjnzf5wc"
THINGSBOARD_HOST    = "192.168.1.88:8080"

thingsboard_url     = "http://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)

sense = SenseHat()
data = {}
next_reading = time.time()

try:
    while True:
        data['temperature'] = sense.get_temperature()
        data['pressure'] = sense.get_pressure()
        data['humidity'] = sense.get_humidity()
        
        #Sending data to Thingsboard
        r = requests.post(thingsboard_url, data=json.dumps(data))

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass




