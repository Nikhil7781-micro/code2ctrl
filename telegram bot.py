import machine
import time
import network
import urequests

ssid= "user_name"
pasd= "password"

bot_token= "bot_token"
chat_id= "your_chatid"
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
