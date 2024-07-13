import board
import busio
import displayio
import digitalio
import time

import analogio
import pwmio
import random

import adafruit_dht

from i2cdisplaybus import I2CDisplayBus

import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
#import adafruit_imageload


light_sensor = analogio.AnalogIn(board.GP26)
pressure_sensor = analogio.AnalogIn(board.GP27)
dhtDevice = adafruit_dht.DHT22(board.GP5)


prev_input = 0

GAIN = 1

displayio.release_displays()

i2c = busio.I2C(board.GP1, board.GP0)
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
#load = adafruit_imageload



#read_snow = ("/creature_snow.pbm")
#read_ice = ("/creature_ice.pbm")
image_data = bytearray()

def snow():
    with open("/creature_snow.pbm", 'rb') as f:
        header = f.readline()
        #assert header == b'P4\n'
        dimensions = f.readline()
        width, height = [int(i) for i in dimensions.split()]
        image_data = bytearray(f.read())
        return imagedata, width, height
        
def ice():
    with open("/creature_ice.pbm", 'rb') as f:
        header = f.readline()
        #assert header == b'P4\n'
        dimensions = f.readline()
        width, height = [int(i) for i in dimensions.split()]
        image_data = bytearray(f.read())
        return imagedata, width, height


#image_data, width, height = read_snow
#image_data, width, height = read_ice

#read_snow = read_pbm("/creature_snow.pbm")

# Create a bitmap the size of the display, initialized to 0 (black)
bitmap = displayio.Bitmap(128, 64, 2)

# Create a two color palette
palette = displayio.Palette(2)
palette[0] = 0x000000  # Black
palette[1] = 0xFFFFFF  # White

# Copy the image data into the display bitmap
for y in range(64):
    for x in range(128):
        byte_index = x // 8 + y * (128 // 8)
        bit_index = x % 8
        pixel = (image_data[byte_index] >> (7 - bit_index)) & 1
        bitmap[x, y] = pixel

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
#display.show(group)
#splash = displayio.Group()
display.root_group = group
# Keep the display on

while True:
    image_data, width, height = load_image("/creature_snow.pbm")
    time.sleep(1000) 