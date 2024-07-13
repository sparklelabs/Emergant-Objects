This code uses 4 buttons or touch sensors on GP 13, 16, 17, 18 and a speaker connected between GP14 and Ground.

```python
# SPDX-FileCopyrightText: 2024 Ariel Churi for Sparkle Labs
# SPDX-License-Identifier: MIT

import board
import digitalio
import pwmio
import time

button0 = digitalio.DigitalInOut(board.GP13)
button0.switch_to_input(pull=digitalio.Pull.DOWN) 
button1 = digitalio.DigitalInOut(board.GP18)
button1.switch_to_input(pull=digitalio.Pull.DOWN) 
button2 = digitalio.DigitalInOut(board.GP16)
button2.switch_to_input(pull=digitalio.Pull.DOWN) 
button3 = digitalio.DigitalInOut(board.GP17)
button3.switch_to_input(pull=digitalio.Pull.DOWN) 

speaker = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=440, variable_frequency=True)

# list of frequencies
tones = [262, 294, 330, 349, 392, 440, 494, 523]

while True:
    if button0.value:
        speaker.frequency = tones[0]
        speaker.duty_cycle = 65535 // 2  # On 50%
    if button1.value:
        speaker.frequency = tones[2]
        speaker.duty_cycle = 65535 // 2  # On 50%
    if button0.value and button1.value:
        speaker.frequency = tones[1]
        speaker.duty_cycle = 65535 // 2  # On 50%
    if button2.value:
        speaker.frequency = tones[4]
        speaker.duty_cycle = 65535 // 2  # On 50%
    if button1.value and button2.value:
        speaker.frequency = tones[3]
    if button3.value:
        speaker.frequency = tones[6]
        speaker.duty_cycle = 65535 // 2  # On 50%
    if button2.value and button3.value:
        speaker.frequency = tones[5]
    if button0.value == 0 and button1.value == 0 and button2.value == 0 and button3.value == 0:
        speaker.duty_cycle = 0  # Off
    time.sleep(.01)
```