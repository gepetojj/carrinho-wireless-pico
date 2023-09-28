from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
import time

app = Microdot()
Response.default_content_type = 'text/html'


@app.route('/')
async def index(request):
    return render_template('index.html')

@app.route('/console')
async def index(request):
    return render_template('console.html')

@app.route('/ws')
@with_websocket
async def send_metrics(request, ws):
    while True:
#         data = await ws.receive()  // Só se tivesse recebendo mensagens
        time.sleep(.1)
        await ws.send({"wifiMenuSelected": True, "erasingMemory": False, "motorsVelocity": -999, "wifiStatus": 0})

@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return "Encerrando conexão..."


if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        pass