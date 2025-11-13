import network
import socket
from machine import Pin
import time


led = Pin(2, Pin.OUT)

ssid = 'user_name'
password = 'wifi_password'


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Connecting to WiFi...", end="")
while not wifi.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nConnected!")
print("IP address:", wifi.ifconfig()[0])


def web_page():
    state = "ON" if led.value() else "OFF"
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>ESP LED Control</title>
</head>
<body>
    <h1>LED is currently: {state}</h1>
    <a href="/?led=on"><button>Turn ON</button></a>
    <a href="/?led=off"><button>Turn OFF</button></a>
    <a href="/?led=blink"><button>Turn BLINKING</button></a>
</body>
</html>
"""
    return html


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Server running, connect to:", wifi.ifconfig()[0])

while True:
    try:
        conn, addr = s.accept()
        print('Client connected from', addr)
        request = conn.recv(1024)
        request = request.decode()
        print('Request:', request)

        if '/?led=on' in request:
            led.value(1)
            print("led is on")
        elif '/?led=off' in request:
            led.value(0)
            print("led is off")
        elif '/?led=blink' in request:
            for i in range(0,10):
                led.toggle()
                print("led is blinking")
                time.sleep_ms(200)
                      
        response = web_page()
        conn.send("HTTP/1.1 200 OK\r\n")
        conn.send("Content-Type: text/html\r\n")
        conn.send("Connection: close\r\n\r\n")
        conn.sendall(response)
        conn.close()
    except OSError as e:
        print("Connection error:", e)
        conn.close()

