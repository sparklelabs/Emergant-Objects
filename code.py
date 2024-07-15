# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# Small edits for Raspberry Pi Pico by Ariel Churi
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, and some white text.
"""

import board
import busio
import time
import digitalio
# display
import displayio
from i2cdisplaybus import I2CDisplayBus
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
# rtc
import adafruit_ds3231
# ultrasonic sensor
import adafruit_hcsr04
# neopixel
import neopixel 
pixels = neopixel.NeoPixel(board.GP13, 2)  # This is the pin for your Neopixels and the number of LEDs in the chain.
# audio
import pwmio
speaker = pwmio.PWMOut(board.GP2, duty_cycle=0, frequency=440, variable_frequency=True)

# the display can mess up the i2c and this resets it.
displayio.release_displays()

# buttons or touchsensors
touch1 = digitalio.DigitalInOut(board.GP17)
touch1.switch_to_input(pull=digitalio.Pull.DOWN)
touch2 = digitalio.DigitalInOut(board.GP16)
touch2.switch_to_input(pull=digitalio.Pull.DOWN)

# ultrasonic sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP14, echo_pin=board.GP15)
my_distance = 0

# rtc
i2c = busio.I2C(board.GP1, board.GP0)  

ds3231 = adafruit_ds3231.DS3231(i2c)
# Set the time by uncommenting this line and setting the year, month, day, hour, minutes, seconds, and day of the week. The last 2 numbers are not used.
# ds3231.datetime = time.struct_time((2024, 7, 9, 9, 6, 0, 1, -1, -1))

# Lookup table for names of days (nicer printing).
days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")

# For the potentiometer.
import analogio
potentiometer = analogio.AnalogIn(board.GP26)

#display
displayio.release_displays()

display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Make the display context
splash = displayio.Group()
display.root_group = splash

# Draw a rectangle
# color_bitmap = displayio.Bitmap(128, 64, 1)
# color_palette = displayio.Palette(1)
# color_palette[0] = 0xFFFFFF  # White
# bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
# splash.append(bg_sprite)

# # Draw a smaller inner rectangle
# inner_bitmap = displayio.Bitmap(124, 60, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0x000000  # Black
# inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=2, y=2)
# splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
myTime = "test"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=0, y=14)
time_area = label.Label(terminalio.FONT, text=myTime, color=0xFFFF00, x=0, y=4)
splash.append(text_area)
splash.append(time_area)

pause = 0.1
for x in range(1,6):
    pixels[0] = (40, 0, 20)
    time.sleep(.02) 
    pixels[0] = (40, 0, 20)
    pixels.fill((0, 0, 0))
    pixels[1] = (0, 20, 60)
    time.sleep(.02) 
    pixels.fill((0, 0, 0))

while True:

    try:
        text_area.text = "SONAR: " + str(sonar.distance)
        # print(sonar.distance)
        # my_distance = sonar.distance
    except RuntimeError:
        print("ERR")
    # if my_distance < 9:
      # print("GET BACK!")

    t = ds3231.datetime
    myTime = "{} {}/{}/{} {}:{:02}:{:02}".format( days[int(t.tm_wday)], t.tm_mon, t.tm_mday, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec )
    time_area.text = str(myTime)
 
    # print(ds3231.datetime)
    # print(t)     # uncomment for debugging
    # print(myTime)
    # print(
    #     "{} {}/{}/{} {}:{:02}:{:02}".format(
    #         days[int(t.tm_wday)], t.tm_mon, t.tm_mday, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec 
    #     )
    # )

    # flash neopixels
    # pixels.fill((0, 20, 0)) # You can send three numbers from 0 to 255.
    # time.sleep(pause)
    # pixels.fill((20, 0, 0)) # It could be red, green, blue or green, red, blue.
    # time.sleep(pause)
    # pixels.fill((0, 0, 20)) # The "fill" command sends the color to all of the LEDs in the line.
    # time.sleep(pause)

    # check buttons
    if touch1.value:
        pixels[1] = (0,20,60)
        for i in range(1000,1500,2):
            speaker.frequency = i
            speaker.duty_cycle = 65535 // 2  # On 50%
            time.sleep(0.001)
        speaker.duty_cycle = 0  # On 50%
    else:
        pixels[1] = (0,0,0)
    if touch2.value:
        pixels[0] = (40,0,20)
        for i in reversed(range(100,700,2)):
            speaker.frequency = i
            speaker.duty_cycle = 65535 // 2  # On 50%
            time.sleep(0.001)
        speaker.duty_cycle = 0
    else:
        pixels[0] = (0,0,0)
      
