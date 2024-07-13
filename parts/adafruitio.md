import ssl
from random import randint
import adafruit_requests
import socketpool
import time
import board
import digitalio
import wifi
import neopixel
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError

pixelsa = neopixel.NeoPixel(board.GP13, 1)    # This is the pin for your Neopixels and the number of LEDs in the chain.
pixelsb = neopixel.NeoPixel(board.GP15, 1)    # This is the pin for your Neopixels and the number of LEDs in the chain.
pixelsa.fill((0, 20, 5)) # You can send three numbers from 0 to 255.
pixelsb.fill((0, 20, 5)) # You can send three numbers from 0 to 255.

# Add a secrets.py to your filesystem that has a dictionary called secrets with "ssid" and
# "password" keys with your WiFi credentials. DO NOT share that file or commit it into Git or other
# source control.
# pylint: disable=no-name-in-module,wrong-import-order
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
# Initialize an Adafruit IO HTTP API object
io = IO_HTTP(aio_username, aio_key, requests)

def checkAdafruitio():
    try:
        # Get the 'temperature' feed from Adafruit IO
        temperature_feed = io.get_feed("temperature")
    except AdafruitIO_RequestError:
        # If no 'temperature' feed exists, create one
        temperature_feed = io.create_new_feed("temperature")
    # Send random integer values to the feed
    random_value = randint(0, 50)
    print("Sending {0} to temperature feed...".format(random_value))
    io.send_data(temperature_feed["key"], random_value)
    print("Data sent!")
    # Retrieve data value from the feed
    print("Retrieving data from temperature feed...")
    received_data = io.receive_data(temperature_feed["key"])
    print("Data from temperature feed: ", received_data["value"])

# checkAdafruitio() # uncomment this line to check the adafruitIO connection.

buttona_feed = io.get_feed("buttona")
buttona = digitalio.DigitalInOut(board.GP12)
buttona.switch_to_input(pull=digitalio.Pull.DOWN)
buttonaPressed = False

buttonb_feed = io.get_feed("buttonb")
buttonb = digitalio.DigitalInOut(board.GP14)
buttonb.switch_to_input(pull=digitalio.Pull.DOWN)
buttonbPressed = False

lastCheckTime = 0
checkTimeInterval = 10

def checkFeed():
    buttonAIOfeed = io.get_feed("buttona")
    buttonBIOfeed = io.get_feed("buttonb")
    print("Button B: ", buttonBIOfeed['last_value'])
    print("Button A: ", buttonAIOfeed['last_value'])
    if int(buttonAIOfeed['last_value']): #check of device A was pressed
        pixelsb.fill((100, 5, 20)) # change device B pixel
    else:
        pixelsb.fill((10,5,40))
    if int(buttonBIOfeed['last_value']):
        pixelsa.fill((100, 5, 20)) # 
    else:
        pixelsa.fill((10,5,40))

checkFeed()
print('Code running...')
pixelsa.fill((0, 40, 5)) # You can send three numbers from 0 to 255.
pixelsb.fill((0, 40, 5)) # You can send three numbers from 0 to 255.

while True:

    if buttona.value and buttonaPressed == False:
        print('Button A pressed')
        buttonaPressed = True
        io.send_data(buttona_feed["key"], 1)
        io.send_data(buttonb_feed["key"], 0)
        pixelsa.fill((10,25,30))
        pixelsb.fill((10,25,30))
    if buttona.value == False and buttonaPressed == True:
        buttonaPressed = False
        
    if buttonb.value and buttonbPressed == False:
        print('Button B pressed')
        buttonbPressed = True
        io.send_data(buttonb_feed["key"], 1)
        io.send_data(buttona_feed["key"], 0)
        pixelsb.fill((10,25,30))
        pixelsa.fill((10,25,30))
    if buttonb.value == False and buttonbPressed == True:
        buttonbPressed = False
        
    if time.monotonic() - lastCheckTime >= checkTimeInterval:
        checkFeed()
        lastCheckTime = time.monotonic()

    time.sleep(.01)

pause = 0.01

