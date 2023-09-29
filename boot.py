import network
from machine import Pin
import time

SSID = "Carrinho Wireless PICO"
SECURITY = 0

builtin_led = Pin("LED", Pin.OUT)


def init_ap():
    builtin_led.on()
    
    nic = network.WLAN(network.AP_IF)
    nic.config(ssid=SSID, security=SECURITY)
    nic.active(True)
    
    print("[WiFi] Modo AP iniciado.")
    print("[WiFi] SSID:", SSID)
    print("[WiFi] IFConfig:", nic.ifconfig())
    
    for x in range(5):
        builtin_led.off()
        time.sleep(.15)
        builtin_led.on()
        time.sleep(.15)
    
    
print("[WiFi] Configurando a conexão WiFi...")
init_ap()