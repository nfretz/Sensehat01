
# Import based on using a physical RPi or the emulator
from sense_emu import SenseHat
# from sense_hat import SenseHat
sense = SenseHat()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
cyan = (0,255,255)

cblue = (0,32,91)
cgreen = (10,134,61)

sense.show_message("Go Canucks", text_colour=cblue, back_colour=cgreen)

sense.clear(0,0,0)
