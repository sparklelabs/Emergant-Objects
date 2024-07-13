# Ultrasonic sensor

```python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP5, echo_pin=board.GP6)

# For the potentiometer.
while True:
    try:
        print(sonar.distance)
        my_distance = sonar.distance
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.01)

    if my_distance > 40:
        print("GET BACK!")
```


![ultrasonic_schematic](ultrasonic_schematic.png)
