import time
import machine
import network
import urequests
import ujson as json

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
    data = {
        "joke": "Juck Noris kann auch mit Python",
        "device": "ESP8266",
        "time": time.time(),
    }
    print(json.dumps(data))
    if wlan.isconnected():
        print(f"Wifi connected")
        try:
            res = urequests.post(
                "https://node-red-f3u9.onrender.com.proxy.gbsl.website/daten", json=data
            )
            print(res.content)
            res.close()
            send = True
        except:
            send = False
    else:
        print(f"Wifi not connected")
        wlan = do_connect(wait=False)
        send = wlan.isconnected()
    time.sleep(5)
