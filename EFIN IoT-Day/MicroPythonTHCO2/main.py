import time
import machine
import network
import urequests
import ujson as json

import ssd1306
import math
from ens import ENS160  # import the device driver
import aht

hour = 0
minute = 0
second = 0
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(64, 48, i2c)
# CO2 sensor
ens160 = ENS160(i2c, temperature=22, humidity=35)  # Initialise the ENS160 module
# temp. and humidity sensor
aht21 = aht.AHT2x(i2c, crc=True)
for i in range(3):
    display.fill(0)
    display.text(f"((({3-i})))", 0, 0, 1)
    display.show()
    time.sleep(1)

# disable access point modus
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)


def wait_for_connection(wifi, timeout=10):
    print("connecting to network...")
    while not wifi.isconnected() and timeout > 0:
        time.sleep(1)
        print(f"waiting for connection {timeout}")
        timeout -= 1
    if wifi.isconnected():
        print("Connected")
    else:
        print("Connection failed!")


def do_connect(wait=True):
    # create wifi sender
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        # wlan.connect(<SSID>, <PSK>)
        wlan.connect("ASYNC", "bv3hmyt3gn1cw")
        if not wait:
            return wlan
        wait_for_connection(wlan)

    print("network config:", wlan.ifconfig())
    return wlan


wlan = do_connect(wait=True)

while True:
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

    data = {
        'temp' : temp, 'hum' : hum, 'eco2' : eco2.value
    }
    print(json.dumps(data))
    if wlan.isconnected():
        print(f"Wifi connected")
        try:
            res = urequests.post("https://node-red-f3u9.onrender.com.proxy.gbsl.website/datenb", json=data)
            res.content
            res.close()
            send = True
        except:
            send = False
        print(send)
    else:
        print(f"Wifi not connected")
        wlan = do_connect(wait=False)
        send = wlan.isconnected()
    
    display.fill(0)
    display.text(f"{round(hum, 1)}%H2O", 0, 0, 1)
    display.text(f"{round(temp, 1)}", 0, 10, 1)
    display.rect(33, 10, 3, 3, 1)
    display.text("C", 37, 10, 1)
    display.text("CO2:", 0, 20, 1)
    display.text(f"{eco2.value}ppm", 0, 30, 1)
    display.text(f"{hour}:{minute}:{second}", 0, 40, 1)
    display.show()
    time.sleep(0.8354444444444444)

    time.sleep(5)
