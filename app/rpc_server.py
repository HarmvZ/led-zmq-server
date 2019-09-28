import time
import zmq
from led_core import LedCore

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
lc = LedCore()
try:
    while True:
        result = "success"
        message = socket.recv_pyobj()
        try:
            result = lc.strip_action(message["action"], **message["kwargs"])
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception as e:
            result = f"An exception of type {type(e).__name__} occurred. Arguments:\n{str(e.args)}"

        #  Send reply back to client
        socket.send_pyobj(result)
except (KeyboardInterrupt, SystemExit):
    socket.destroy()