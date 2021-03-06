import websocket
import thread
import time

def on_message(ws, message):
    print message
    updateMes = message[message.index(':')+2:255]
    print updateMes
    if updateMes[0:5] == '!chat':
        command = updateMes[updateMes.index(' ')+1:255]
        print command

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print('Connected.')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://104.236.172.36:8001",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()
