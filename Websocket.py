import websocket, json  

cc = 'btcusd'
interval = '1m'

socket = f'wss://stream.binance.com:9443/ws/{cc}t@kline_{interval}'

socket 

def on_message(ws, message):
    print(message)

def on_close(ws):
    print('Connection Closed')

ws = websocket.WebSocketApp(socket, on_message = on_message, on_close = on_close)

ws.run_forever()