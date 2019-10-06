using System;
using System.Threading;
using NetMQ;
using NetMQ.Sockets;

namespace NetMQApp
{
    class Program
    {
        static void Main(string[] args)
        {
            string sPort = "5555";

            if (args.Length == 0)
            {
                Console.WriteLine("Requires one argument (a number):");
                Console.WriteLine("1    client");
                Console.WriteLine("2    server");
                Console.WriteLine("3    pubsub subscriber");
                Console.WriteLine("4    pubsub publisher");
                return;
            }

            if (args[0] == "1")             // client
            {
                ThreadStart ref1 = new ThreadStart(() =>
                {
                    Thread th = Thread.CurrentThread;
                    th.Name = "ClientThread";
                    //var domain = Thread.GetDomain();
                    var domainId = Thread.GetDomainID();
                    Console.WriteLine("{0} priority:{1} state:{2} domainId:{3} threadId:{4}", th.Name, th.Priority, th.ThreadState, domainId, th.ManagedThreadId);
                    // client
                    Console.WriteLine("Starting client...");
                    using (var client = new RequestSocket())
                    {
                        for (int i = 0; i < 10; ++i)
                        {
                            client.Connect("tcp://127.0.0.1:" + sPort);
                            //Console.WriteLine("Sending request {0} ...", i);
                            client.SendFrame(string.Format("Hello {0}", i));
                            var msg = client.ReceiveFrameString();
                            Console.WriteLine("Received reply {0} [ {1} ]", i, msg);
                        }
                    }
                });
                Thread thread1 = new Thread(ref1);
                thread1.Start();
            }
            else if (args[0] == "2")        // server
            {
                ThreadStart ref2 = new ThreadStart(() =>
                {
                    Thread th = Thread.CurrentThread;
                    th.Name = "ServerThread";
                    // server
                    Console.WriteLine("Starting server...");
                    using (var server = new ResponseSocket())
                    {
                        while (true)
                        {
                            server.Bind("tcp://*:" + sPort);
                            string msg = server.ReceiveFrameString();
                            Console.WriteLine("From Client: {0}", msg);
                            Thread.Sleep(1000);
                            server.SendFrame("World");
                        }
                    }
                });
                Thread thread2 = new Thread(ref2);
                thread2.Start();
            }
            else if (args[0] == "3")        // pub-sub subscriber
            {
                ThreadStart ref3 = new ThreadStart(() =>
                {
                    Thread th = Thread.CurrentThread;
                    th.Name = "SubscriberThread";
                    // pub-sub subscriber
                    Console.WriteLine("Starting subscriber...");
                    using (var subscriber = new SubscriberSocket())
                    {
                        subscriber.Connect("tcp://127.0.0.1:" + sPort);
                        subscriber.Subscribe("A");

                        while (true)
                        {
                            var topic = subscriber.ReceiveFrameString();
                            var msg = subscriber.ReceiveFrameString();
                            Console.WriteLine("From Publisher: {0} {1}", topic, msg);
                        }
                    }
                });
                Thread thread3 = new Thread(ref3);
                thread3.Start();
            }
            else if (args[0] == "4")        // pub-sub publisher
            {
                ThreadStart ref4 = new ThreadStart(() =>
                {
                    Thread th = Thread.CurrentThread;
                    th.Name = "PublisherThread";
                    // pub-sub publisher
                    Console.WriteLine("Starting publisher...");
                    using (var publisher = new PublisherSocket())
                    {
                        publisher.Bind("tcp://*:" + sPort);

                        int i = 0;

                        while (true)
                        {
                            publisher
                                .SendMoreFrame("A") // Topic
                                .SendFrame(i.ToString()); // Message

                            i++;
                            Thread.Sleep(1000);
                        }
                    }
                });
                Thread thread4 = new Thread(ref4);
                thread4.Start();
            }

        }

    } // class
} // namespace
