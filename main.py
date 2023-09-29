from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
from machine import Pin
import controls
import network
import gc

right_wheel = controls.Motor(6, 7, 8)
left_wheel = controls.Motor(27, 26, 22)
motors_velocity = 255

app = Microdot()
Response.default_content_type = 'text/html'

@app.route("/")
async def index(request):
    return render_template('index.html')

@app.route("/console")
async def console(request):
    return render_template('console.html')

@app.route("/changeVel")
async def change_vel(request):
    args = request.args
    velocity = int(args["vel"])
    
    if velocity < 0 or velocity > 100:
        velocity = 100
    
    motors_velocity = velocity
    return {"velocidade": motors_velocity}

@app.route("/ws")
@with_websocket
async def websocket(request, ws):
    while True:
        data = await ws.receive()
        data = str(data)
        
        if data in controls.AVAILABLE_CONTROLS:
            controls.move(data, right_wheel, left_wheel, motors_velocity)
            
        wlan = network.WLAN(network.AP_IF)
        metrics = "{}::{}::{}::{}::{}::{}::{}".format(wlan.status(), motors_velocity, 0, gc.mem_free(),
                                                      gc.mem_alloc(), wlan.ifconfig()[0], str(wlan.config("mac")))
        await ws.send(metrics)

@app.route("/shutdown")
def shutdown(request):
    print("[Sys] Desligando servidor...")
    print("[Sys] Conexão WiFi será mantida!")
    request.app.shutdown()
    
    builtin_led = Pin("LED", Pin.OUT)
    for x in range(7):
        builtin_led.off()
        time.sleep(.15)
        builtin_led.on()
        time.sleep(.15)
    
    return "Encerrando conexão..."


print("[Sys] Servidor iniciado.")
app.run(host="0.0.0.0", port=80)