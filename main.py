
import json
import requests
from time import sleep

# Import based on using a physical RPi or the emulator
#from sense_emu import SenseHat
from sense_hat import SenseHat

# Constants

API_KEY             = "jrAlYyNVNG1fYX6Woxky"
THINGSBOARD_HOST    = "192.168.1.82:8080"

thingsboard_url     = "http://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)

sense = SenseHat()
data = {}

while True:
    data['temperature'] = sense.get_temperature()
    data['pressure'] = sense.get_pressure()
    data['humidity'] = sense.get_humidity()
    r = requests.post(thingsboard_url, data=json.dumps(data))
    print (str(data))
    sleep(5)


