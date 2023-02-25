import time
import machine
import ssd1306
import math
from ens import ENS160  # import the device driver
import aht

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(64, 48, i2c)
# CO2 sensor
ens160 = ENS160(i2c, temperature=22, humidity=35)   # Initialise the ENS160 module
# temp. and humidity sensor
aht21 = aht.AHT2x(i2c, crc=True)

display.fill(0)
display.text('Loading...', 0, 0, 1)
display.show()
time.sleep(3)
second = 0
minute = 0
hour = 0
while True:
    Z1 = time.time()
    # Read from the sensor
    aqi = ens160.aqi
    tvoc = ens160.tvoc
    eco2 = ens160.eco2
    hum = aht21.humidity
    temp = aht21.temperature
    second += 1
    if second == 60:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1

    # treat invalid sensor states
    if aht21.status == 0:  # invalid
        aht21.reset()

    if ens160.status_validity_flag == 3:  # invalid
        ens160.reset()

    display.fill(0)
    display.text(f'{round(hum, 1)}%H2O', 0, 0, 1)
    display.text(f'{round(temp, 1)}', 0, 10, 1)
    display.rect(33, 10, 3, 3, 1)
    display.text('C', 37, 10, 1)
    display.text('CO2:', 0, 20, 1)
    display.text(f'{eco2.value}ppm', 0, 30, 1)
    display.text(f'{hour}:{minute}:{second}', 0, 40, 1)
    display.show()

    time.sleep(1 - Z1)
