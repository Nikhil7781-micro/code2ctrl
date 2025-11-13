import machine
import network
import time

wifi_name="your_wifi_name"
passw="your_password"
 
wlan= network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_name,passw)

print("connecting to wifi......")
while not wlan.isconnected():
    time.sleep_ms(100)
    print("connected",wlan.ifconfig()[0])
    

