import machine
import time

touch = machine.TouchPad(machine.Pin(4))
led = machine.Pin(2, machine.Pin.OUT)

threshold = 300   
while True:
    value = touch.read()     
    print("Touch Value:", value)
    
    if value < threshold:
        led.on()
    else:
        led.off()
    
    time.sleep(0.2)
