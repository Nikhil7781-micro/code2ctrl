import machine
import time
import network
import urequests

ssid= "LAVA LXX504"
pasd= "00778100"

bot_token= "7548858775:AAHpbKqF6S8W5_g5fGfPMihJoCxjL0NOb_o"
chat_id= "6045281845"
messg= "Alert! someone detected"

led= machine.Pin(2, machine.Pin.OUT)
pir= machine.Pin(26,machine.Pin.IN)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid,pasd)

if wifi.isconnected():
    print("connected")
else:
    pass

def message(messag):
    url= f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload= {"chat_id": chat_id, "text": messag}
    try:
        response= urequests.post(url, json=payload)
        print("Telegram response:", response.text)
        response.close()
    except Exception as e:
        print("exit")
        
while True:
    if pir.value():
        message(messg)
        print("motion")
        led.toggle()
        time.sleep(3)
    time.sleep_ms(200)