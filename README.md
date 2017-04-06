# HWYD WS2811 BRIDGE v3
### Prototyping with LED's and the Rasperry PI

##

This Raspberry Pi shield is designed with LED prototyping in mind. We love building with Neopixels and needed a tool that was easy to use.  attaches to the GPIO pins of your RPi and acts as a WS281X Bridge between your dreams and the LED's of your choice. The shield allows us to streamline our led ideas without the need of a breadboard, cobbler setup and extra wires.

![v3](http://imgur.com/BhLXpe6.png)

##### A note for v3 users: we've updated the pinout order on v3 to GND, PWR, DIN.

##
##
##

# Features
* Supports Raspbbery Pi A, B/B+, 2, 3, Zero and Zero W!
* Works with any WS2811 / WS2812 LED's and Neopixels (strips too)
* 3 pin Molex slots for easily swapping out your LED's
* 100uf capacitor to protect against surges while powering
* Based off 74hCT125N
* Inspired by adafruit Neopixels and Fadecandy.

##
##
##

# BUILD GUIDE
###### If you purchase our board unassembled. Please follow the guide below. Note that v2 and v3 boards have different pinouts for the LED strips; everything else is the same.

##

![neopixels-project](http://i.imgur.com/BNCCEuD.png)

##

We chose Raspberry Pi for it's speed, networking capabilities, threading etc. Also we like the flexbility Python offers for web and data minded projects.

##

### STEP 1: PARTS LIST
![parts-list](http://i.imgur.com/g5a3GXF.png)
```
* HWYD Board
* Raspberry Pi
* 3pin Molex
* Power Jack
* IC
* IC Socket
* 2x20 Headers
* 100uF Capacitor
```

##
##

### STEP 2: SOLDER
![solder-tip](http://i.imgur.com/WxIqGKk.png)
```
Solder it up. This version of the board has 5 parts and should take 
10-15 minute to complete.
```
##

### STEP 3: ATTACH
![plugged-in](http://i.imgur.com/YSvPC3c.png)

### V2 boards
```
DIN, POWER, GROUND
```

### V3 boards
```
GND, PWR, DIN
```

##
##

# INSTALLING DRIVERS
We are using the rpi_ws281 library from jgarff. You can find a more detailed version of the [driver installation guide from adafruit](https://learn.adafruit.com/neopixels-on-raspberry-pi/software).

### STEP 1: Update your Pi
```
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
```

### STEP 2: Download the rpi_ws281 library
```
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
```

### STEP 3: Install
```
cd python
sudo python setup.py install
```

### STEP 4: Run an example
```
cd python/examples
sudo python strandtest.py
```

##
##

# Where do I get one?
Let us know, It's only $10!
https://www.tindie.com/products/areaofeffect/raspberry-pi-ws281x-led-shield/

![aura](http://i.imgur.com/wi87srU.gif)

##
##

###### Radical Networks, NYC Creative Tech Week, Halloween Pixels, [kandizzy/hotline-bling](https://github.com/kandizzy/hotline-bling) <br/>