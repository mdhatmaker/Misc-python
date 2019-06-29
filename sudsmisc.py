from suds.client import Client
from xml2dictionary import *

url = 'http://www.webservicex.net/WeatherForecast.asmx?WSDL'
url = 'http://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl'
url = 'http://www.webservicex.net/stockquote.asmx?WSDL'
def createClient(url, methodName):
    client = Client(url)

    #temp = str(client)

    client.factory.create(methodName)
    return client

def printMethods(client):
    print
    for method in client.wsdl.services[0].ports[0].methods.values():
        print '%s(%s)' % (method.name, ', '.join('%s: %s' % (part.type, part.name) for part in method.soap.input.body.parts))
    return

def xml2dict(xml):
    root = ElementTree.XML(xml)
    xmldict = XmlDictConfig(root)
    return xmldict

client = createClient('http://www.webservicex.net/stockquote.asmx?WSDL', 'GetQuote')
printMethods(client)
quote = client.service.GetQuote('MSFT')
#print quote
xmldict = xml2dict(quote)
#print xmldict
#print
for k in xmldict['Stock']:
    print k, xmldict['Stock'][k]
    
client = createClient('http://www.webservicex.net/LondonGoldFix.asmx?WSDL', 'GetLondonGoldAndSilverFix')
printMethods(client)
fix = client.service.GetLondonGoldAndSilverFix()
print fix
#xmldict = xml2dict(fix)
#print xmldict

client = createClient('http://www.webservicex.net/RealTimeMarketData.asmx?WSDL', 'Quote')
printMethods(client)
