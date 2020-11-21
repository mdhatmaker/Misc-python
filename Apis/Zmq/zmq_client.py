import zmq

port = "5555"

context = zmq.Context()

# Socket to talk to server
print("Connecting to ZeroMQ server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)

# Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s ..." % request)
    #socket.send(b"Hello")
    socket.send_string("Hello")

    # Get the reply
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))

