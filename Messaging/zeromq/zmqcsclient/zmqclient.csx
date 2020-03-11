//#load "setup.csx"
//#r "nunit.core.dll"
//#r "nunit.core.interfaces.dll"
#r "system.dll"
#r "netmq.dll"

using System;

/*
var path = "MyUnitTests.dll";
var runner = TestSetup.GetRunner(new[] {path});
var result = runner.Run(new ConsoleListener(msg => Console.WriteLine(msg)), TestFilter.Empty, true, 	LoggingThreshold.All);

Console.ReadKey();
*/

class Program
{
    static void Main(string[] args)
    {
        using (var client = new RequestSocket())
        {
            client.Connect("tcp://127.0.0.1:5556");
            client.SendFrame("Hello");
            var msg = client.ReceiveFrameString();
            Console.WriteLine("From Server: {0}", msg);
        }
    }
}


