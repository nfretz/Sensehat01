
import json
import requests
import time

# Import based on using a physical RPi or the emulator
#from sense_hat import SenseHat
from sense_emu import SenseHat

# Constants
INTERVAL            = 2  #Data capture and upload interval in seconds.
API_KEY             = "bfsfmi1v6oo29qq69msr"   #Key for RPi
THINGSBOARD_HOST    = "192.168.1.223:8080"

telemetry_url     = "http://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)
attribute_url     = "http://{0}/api/v1/{1}/attributes".format(THINGSBOARD_HOST, API_KEY)

sense = SenseHat()
data = {}
next_reading = time.time()

try:
    while True:
        data['temperature'] = sense.get_temperature()
        data['pressure'] = sense.get_pressure()
        data['humidity'] = sense.get_humidity()

        
        #Sending data to Thingsboard
        r = requests.post(telemetry_url, data=json.dumps(data))
        time.sleep(1)

        #Receiving data from Thingsboard
        r = requests.get(attribute_url)
        msg = r.text

        print(msg)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass




