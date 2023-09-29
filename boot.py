import network
from machine import Pin
import time
import gc

gc.enable()

SSID = "Carrinho Wireless PICO"
SECURITY = 0

builtin_led = Pin("LED", Pin.OUT)


def init_ap():
    builtin_led.on()
    
    nic = network.WLAN(network.AP_IF)
    nic.config(ssid=SSID, security=SECURITY)
    nic.active(True)
    
    print("[Boot] Modo AP iniciado.")
    print("[Boot] SSID:", SSID)
    print("[Boot] IFConfig:", nic.ifconfig())
    
    for x in range(5):
        builtin_led.off()
        time.sleep(.15)
        builtin_led.on()
        time.sleep(.15)
    
    
print("[Boot] Configurando a conexão WiFi...")
init_ap()