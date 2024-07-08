# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# Small edits for Raspberry Pi Pico by Ariel Churi
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, and some white text.
"""

# display
import board
import busio
import displayio
from i2cdisplaybus import I2CDisplayBus
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import time
import adafruit_ds3231

displayio.release_displays()

# rtc
i2c = busio.I2C(board.GP1, board.GP0)  

ds3231 = adafruit_ds3231.DS3231(i2c)
# Set the time by uncommenting this line and setting the year, month, day, hour, seconds, and day of the week. The last 2 numbers are not used.
# ds3231.datetime = time.struct_time((2024, 7, 7, 20, 16, 0, 4, -1, -1))

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
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=40)
time_area = label.Label(terminalio.FONT, text=myTime, color=0xFFFF00, x=0, y=4)
splash.append(text_area)
splash.append(time_area)

while True:
    text_area.text = str(potentiometer.value)

    t = ds3231.datetime
    myTime = "{} {}/{}/{} {}:{:02}:{:02}".format( days[int(t.tm_wday)], t.tm_mon, t.tm_mday, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec )
    time_area.text = str(myTime)
 
    # print(ds3231.datetime)
    # print(t)     # uncomment for debugging
    print(myTime)
    # print(
    #     "{} {}/{}/{} {}:{:02}:{:02}".format(
    #         days[int(t.tm_wday)], t.tm_mon, t.tm_mday, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec 
    #     )
    # )
    time.sleep(.1)  # wait a second    

