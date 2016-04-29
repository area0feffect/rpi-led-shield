#HWYD WS2811 BRIDGE: GUIDE
###Prototyping with Neopixels and the Rasperry PI 

This is a guide for using our Raspberry Pi shield designed with LED prototyping in mind. It attaches to the GPIO pins of your Raspberry Pi and acts as a WS2811 Bridge between LED's of your choice. We love prototyping with Neopixels and needed a tool that was easy to use. The shield allows us to get our prototypes going right away without the need of a breadboard, cobbler setup and extra wires.

<br/>

![project](http://i.imgur.com/7fsSMto.png)

<br/>
<br/>

#NOTE
* Supports Raspbbery Pi A, B/B+, 2 and 3.
* Works with any WS2811 / WS2812 LED's and Neopixels
* 3 and 4 pin Molex slots for easily swapping out your LED's
* 100uf capacitor to protect against surges while powering
* Inspired by adafruit Neopixels and Fadecandy.


<br/>
<br/>


#BUILD GUIDE
![neopixels-project](http://i.imgur.com/BNCCEuD.png)

<br/>

We chose Raspberry Pi for it's speed, networking capabilities, 
threading etc. Also we like the flexbility Python offers for web 
and data minded projects.

<br/>

###STEP 1: PARTS LIST
![parts-list](http://i.imgur.com/g5a3GXF.png)
<pre>
* HWYD Board
* Raspberry Pi
* 3pin Molex
* Power Jack
* IC
* IC Socket
* 2x20 Headers
* 100uF Capacitor
</pre>

<br/>
<br/>

###STEP 2: SOLDER
![solder-tip](http://i.imgur.com/WxIqGKk.png)
<pre>
Solder it up. This version of the board has 5 parts and should take 
10-15 minute to complete.
</pre>

<br/>

###STEP 3: ATTACH
![plugged-in](http://i.imgur.com/YSvPC3c.png)
<pre>
DIN, POWER, GROUND
</pre>

<br/>

#INSTALLING DRIVERS
We are using the rpi_ws281 library from jgarff. You can find a more detailed version of the [driver installation guide from adafruit](https://learn.adafruit.com/neopixels-on-raspberry-pi/software).



###STEP 1: Update your Pi
<pre>
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
</pre>

###STEP 2: Download the rpi_ws281 library
<pre>
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
</pre>

###STEP 3: Install
<pre>
cd python
sudo python setup.py install
</pre>

###STEP 4: Run an example
<pre>
cd python/examples
sudo python strandtest.py
</pre>

<br/>
<br/>
<br/>
<br/>

#Where do I get one?
Let us know, It's only $10!

![aura](http://i.imgur.com/wi87srU.gif)

<br/>

######Radical Networks, NYC Creative Tech Week, Halloween Pixels, [kandizzy/hotline-bling](https://github.com/kandizzy/hotline-bling) <br/>