# Real time clock ds3231

A _real time clock_ keeps the actual time once you set it.

Connect the clock chip to power and ground and the SDA to pin GP10 and the SCL GP11.

(This is the RTC I used)[https://www.amazon.com/dp/B09KPC8JZQ]

This code is based on this guide: [Adafruit DS3231 Precision RTC Breakout](https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/circuitpython)

```python
import time
import board
import busio
import adafruit_ds3231

i2c = busio.I2C(board.GP11, board.GP10)  
ds3231 = adafruit_ds3231.DS3231(i2c)

# Set the time by uncommenting this line and setting the year, month, day, hour, seconds, and day of the week. The last 2 numbers are not used.
# ds3231.datetime = time.struct_time((2024, 4, 19, 20, 6, 0, 4, -1, -1))

# Lookup table for names of days (nicer printing).
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

while True:
    t = ds3231.datetime
    # print(ds3231.datetime)
    # print(t)     # uncomment for debugging
    print(
        "The date is {} {}/{}/{}".format(
            days[int(t.tm_wday)], t.tm_mon, t.tm_mday, t.tm_year
        )
    )
    print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))
    time.sleep(1)  # wait a second    
```
