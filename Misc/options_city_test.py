from socket import *

print 'creating socket...'
s = socket(AF_INET, SOCK_STREAM)

print 'connecting...'
host = '10.46.48.54'
port = 9031
s.connect((host, port))

print 'sending logon...'
s.send('LogOn MN8 nashed v2.3')

print 'reading data...'
i = 0
while (1):
    data = s.recv(1024)
    i += 1
    print data
    #if (i < 5):
    #    print data
    if not data:
        break
    print 'received', len(data), 'bytes'
    if data.startswith('Heartbeat'):
        print 'sending heartbeatack...'
        s.send('HeartbeatAck')


s.close()

