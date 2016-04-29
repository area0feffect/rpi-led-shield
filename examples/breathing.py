# NeoPixel library strandtest example
# This is a simple breathing example
#

import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

#quick breathing hack
global currentBrightness
currentBrightness = 10

global currentDirection
currentDirection = 1

# Define functions which animate LEDs in various ways.
def breath(strip, color, speed, wait_ms=50):
	global currentBrightness
	global currentDirection

	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.setBrightness(currentBrightness)
		strip.show()

	#increase and decrease the brightness linearly for
	# a pusle or 'breathing' effect
	currentBrightness += currentDirection * speed;
	if (currentBrightness >= 255):
		currentDirection *= -1
	elif ( currentBrightness <= 10):
		currentDirection *= -1


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:

		# Color wipe animations.
		breath(strip, Color(0, 0, 255), 5)  # G, R, B and speed