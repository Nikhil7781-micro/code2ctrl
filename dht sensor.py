import machine
import time
import dht

dht_pin= machine.Pin(12)
sensor= dht.DHT11(dht_pin)

while True:
    try:
        time.sleep(2)
        s= sensor.measure()
        print(s)
        t= sensor.temperature()
        h= sensor.humidity()
        
        print("temp: %3.1f c" %t)
        print("hum: %3.if%%" %h)
       
        
    except Exception as e:
        
        print("sensor failed")
        