# RGB LEDs

## Links
https://learn.adafruit.com/rgb-led-strips/circuitpython-code

## Code
### This code cycles between three different colors.

```python
# SPDX-License-Identifier: MIT
# This code cycles between three different colors.

import board
import pwmio
import time
from adafruit_simplemath import map_range # Install this library in your Pico's lib folder. https://circuitpython.org/libraries.

red = pwmio.PWMOut(board.GP19)
green = pwmio.PWMOut(board.GP21)
blue = pwmio.PWMOut(board.GP20)

def duty_cycle(percent):
    # return int(map_range(percent, 0, 100, 0, 65535)) # use this if your LED has a common cathode.
    return int(map_range(percent, 100, 0, 0, 65535)) # use this if your LED has a common anode.


while True:
    red.duty_cycle = duty_cycle(25)
    green.duty_cycle = duty_cycle(05)
    blue.duty_cycle = duty_cycle(100)
    time.sleep(.3)
    red.duty_cycle = duty_cycle(100)
    green.duty_cycle = duty_cycle(25)
    blue.duty_cycle = duty_cycle(05)
    time.sleep(.3)
    red.duty_cycle = duty_cycle(05)
    green.duty_cycle = duty_cycle(100)
    blue.duty_cycle = duty_cycle(25)
    time.sleep(.3)
```

### Three buttons for red, green, and blue

```python
# SPDX-License-Identifier: MIT
# Three buttons for red, green, and blue

import board
import pwmio
import digitalio
import time
from adafruit_simplemath import map_range # Install this library in your Pico's lib folder. https://circuitpython.org/libraries.

red = pwmio.PWMOut(board.GP19)
green = pwmio.PWMOut(board.GP21)
blue = pwmio.PWMOut(board.GP20)

def duty_cycle(percent):
    # return int(map_range(percent, 0, 100, 0, 65535)) # use this if your LED has a common cathode.
    return int(map_range(percent, 100, 0, 0, 65535)) # use this if your LED has a common anode.

button0 = digitalio.DigitalInOut(board.GP13)
button0.switch_to_input(pull=digitalio.Pull.DOWN) 
button1 = digitalio.DigitalInOut(board.GP18)
button1.switch_to_input(pull=digitalio.Pull.DOWN) 
button2 = digitalio.DigitalInOut(board.GP16)
button2.switch_to_input(pull=digitalio.Pull.DOWN) 

while True:
    if button0.value:
        red.duty_cycle = duty_cycle(100)
    else:
        red.duty_cycle = duty_cycle(0)
    if button1.value:
        green.duty_cycle = duty_cycle(100)
    else:
        green.duty_cycle = duty_cycle(0)
    if button2.value:
        blue.duty_cycle = duty_cycle(100)
    else:
        blue.duty_cycle = duty_cycle(0)
    time.sleep(.01)
```

### Cycle through a list of named colors

```python
# SPDX-License-Identifier: MIT

import board
import pwmio
import time
from adafruit_simplemath import map_range # Install this library in your Pico's lib folder. https://circuitpython.org/libraries.

red = pwmio.PWMOut(board.GP19)
green = pwmio.PWMOut(board.GP21)
blue = pwmio.PWMOut(board.GP20)

def duty_cycle(percent):
    # return int(map_range(percent, 0, 100, 0, 65535)) # use this if your LED has a common cathode.
    return int(map_range(percent, 100, 0, 0, 65535)) # use this if your LED has a common anode.

red.duty_cycle = duty_cycle(0)
green.duty_cycle = duty_cycle(0)
blue.duty_cycle = duty_cycle(0)

colors = {
    "rose": [100,05,15], "cerulean": [05,20,100], "chartreuse": [10,100,10], "violet": [50,10,100], "indigo": [0,0,100], "turmeric": [100,100,0], "ochre": [20,20,1], "vermillion": [100,01,05]
    }

while True:
    for i in colors:
        red.duty_cycle = duty_cycle(colors[i][0])
        green.duty_cycle = duty_cycle(colors[i][1])
        blue.duty_cycle = duty_cycle(colors[i][2])
        time.sleep(.5)
```