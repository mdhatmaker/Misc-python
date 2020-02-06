from suds.client import Client

url = 'http://mssoapinterop.org/asmx/simple.asmx?WSDL'
client = Client(url)

temp = str(client)

for method in client.wsdl.services[0].ports[0].methods.values():
    print '%s(%s)' % (method.name, ', '.join('%s: %s' % (part.type, part.name) for part in method.soap.input.body.parts))

