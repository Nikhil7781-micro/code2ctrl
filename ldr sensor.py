import machine
import time


ldr_pin= machine.Pin(12,machine.Pin.IN)

adc= machine.ADC(12)

adc.atten(machine.ADC.ATTN_11DB) 

while True:
    
    ldr_value = adc.read()
    print(f"ldr value: {ldr_value}")
    
    

