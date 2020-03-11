from suds.client import Client

url = 'http://www.webservicex.net/WeatherForecast.asmx?WSDL'
url = 'http://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl'
client = Client(url)

temp = str(client)

for method in client.wsdl.services[0].ports[0].methods.values():
    print '%s(%s)' % (method.name, ', '.join('%s: %s' % (part.type, part.name) for part in method.soap.input.body.parts))

client.factory.create(u'GetWeatherByZipCode')
client.service.GetWeatherByZipCode('46383')
