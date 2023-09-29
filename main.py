from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
import controls

right_wheel = controls.Motor(12, 13)
left_wheel = controls.Motor(14, 15)

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/')
async def index(request):
    return render_template('index.html')

@app.route('/console')
async def console(request):
    return render_template('console.html')

@app.route('/ws')
@with_websocket
async def websocket(request, ws):
    while True:
        data = await ws.receive()
        data = str(data)
        
        if data in controls.AVAILABLE_CONTROLS:
            controls.move(data, right_wheel, left_wheel)
                
        await ws.send("{'wifiMenuSelected': true, 'erasingMemory': false, 'motorsVelocity': -999, 'wifiStatus': 0}")

@app.route('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'Encerrando conexão...'


app.run(host="0.0.0.0", port=80, debug=True)