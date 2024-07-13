# Audio

The following code creates a series of tones with a speaker attached to GP14 and ground.

```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials PWM with variable frequency speaker example"""
import time
import board
import pwmio

speaker = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=440, variable_frequency=True)

while True:
    for f in (262, 294, 330, 349, 392, 440, 494, 523):
        speaker.frequency = f
        speaker.duty_cycle = 65535 // 2  # On 50%
        time.sleep(0.25)  # On for 1/4 second
        speaker.duty_cycle = 0  # Off
        time.sleep(0.05)  # Pause between notes
    time.sleep(0.5)
```

This code emits tone based on a potentiometer on GP26/A0

```python
import time
import board
import pwmio
import analogio
from adafruit_simplemath import map_range

potentiometer = analogio.AnalogIn(board.GP26)

speaker = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=440, variable_frequency=True)

while True:
    freq = int(map_range(potentiometer.value, 0, 65535, 30, 1200))
    # print(freq)
    speaker.frequency = freq
    speaker.duty_cycle = 65535 // 2  # On 50%
    time.sleep(0.0)
```

Squeeks!

```python
import time
import board
import pwmio
import analogio
from adafruit_simplemath import map_range

potentiometer = analogio.AnalogIn(board.GP26)

speaker = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=440, variable_frequency=True)

while True:
    for i in range(1000,1800,2):
        speaker.frequency = i
        speaker.duty_cycle = 65535 // 2  # On 50%
        print(i)
        time.sleep(0.00)
    # print(freq)
    speaker.duty_cycle = 0  # On 50%
    time.sleep(.05)
    for i in range(1800,1000,-1):
        speaker.frequency = i
        speaker.duty_cycle = 65535 // 2  # On 50%
        print(i)
        time.sleep(0.00)
    speaker.duty_cycle = 0  # On 50%
    time.sleep(.15)
    for i in range(300,1000,1):
        speaker.frequency = i
        speaker.duty_cycle = 65535 // 2  # On 50%
        print(i)
        time.sleep(0.00)
    speaker.duty_cycle = 0  # On 50%
    time.sleep(2)# Audio
```
