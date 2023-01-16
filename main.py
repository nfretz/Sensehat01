
# Import based on using a physical RPi or the emulator
#from sense_emu import SenseHat
from sense_hat import SenseHat
sense = SenseHat()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
cyan = (0,255,255)

cblue = (0,32,91)
oblue = (4,30,66)
cgreen = (10,134,61)
oorange = (252,76,0)

sense.show_message("Oilers suck", text_colour=oblue, back_colour=oorange)

sense.clear(0,0,0)
