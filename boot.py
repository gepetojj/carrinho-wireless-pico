import network


def init_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(ssid="Carrinho Wireless PICO")

    while ap.active() == False:
        pass

    print("[WiFi] Conexao AP iniciada")
    print(ap.ifconfig())
    

print("[WiFi] Iniciando WiFi...")
init_ap()
