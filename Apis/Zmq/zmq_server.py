import zmq
import time
import sys

port = "5555"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

print("\nZeroMQ Server\n")
print("Waiting for message...", end='', flush=True)
while True:
    # Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    # Do some 'work'
    time.sleep(1)

    # Send reply back to client
    #socket.send(b"World")
    socket.send_string("World")

    print("Waiting for message...", end='', flush=True)
