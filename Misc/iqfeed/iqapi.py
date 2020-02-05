"""
Credit: Michael Halls-Moore
Url:    https://www.quantstart.com/articles/Downloading-Historical-Intraday-US-
        Equities-From-DTN-IQFeed-with-Python
        
I simply wrapped the logic into a class. 
Will possibly extend for live feeds.
@author: Luke Patrick James Tighe
"""

import datetime
import socket
import os.path
import pandas as pd

"""
IQ DTN Feed Historical Symbol Download.
Downloads the symbol data in CSV format and stores it in a local directroy.
If we already have the symbol data downloaded, it will not hit IQ DTN Feed again,
it will simple use the local data.
To flush the local CSV file, simply delete the directory.
Constructor enables to specify a start and end date for the symbol data as well
as the frequency. Great for making sure data is consistent.
Simple usage example:
    from iqfeed import historicData
    dateStart = datetime.datetime(2014,10,1)
    dateEnd = datetime.datetime(2015,10,1)        
        
    iq = historicData(dateStart, dateEnd, 60)
    symbolOneData = iq.download_symbol(symbolOne)
    
"""
class historicData:

    # 
    def __init__(self, startDate, endDate, timeFrame=60, beginFilterTime='', endFilterTime=''):
        
        self.startDate = startDate.strftime("%Y%m%d %H%M%S")
        self.endDate = endDate.strftime("%Y%m%d %H%M%S")
        #self.timeFrame = str(timeFrame)
        self.timeFrame = timeFrame
        self.beginFilterTime = beginFilterTime          # format "HHmmSS"
        self.endFilterTime = endFilterTime              # format "HHmmSS"
        # We dont want the download directory to be in our source control
        #self.downloadDir = "./MarketData/"
        self.downloadDir = ""
        self.host = "127.0.0.1"  # Localhost
        self.port = 9100  # Historical data socket port


    def read_historical_data_socket(self, sock, recv_buffer=4096):
        """
        Read the information from the socket, in a buffered
        fashion, receiving only 4096 bytes at a time.
    
        Parameters:
        sock - The socket object
        recv_buffer - Amount in bytes to receive per read
        """
        buffer = ""
        data = ""
        while True:
            data = sock.recv(recv_buffer)
            buffer += data
    
            # Check if the end message string arrives
            if "!ENDMSG!" in buffer:
                break
       
        # Remove the end message string
        buffer = buffer[:-12]
        return buffer


#HIT,[Symbol],[Interval],[BeginDate BeginTime],[EndDate EndTime],[MaxDatapoints],[BeginFilterTime],[EndFilterTime],[DataDirection],[RequestID],[DatapointsPerSend],[IntervalType]<CR><LF> 

    def get_message_minute(self, symbol):
        #message = "HIT,{0},{1},{2},{3},,093000,160000,s\n".format(symbol, self.timeFrame, self.startDate, self.endDate)
        #message = "HIT,{0},{1},{2},{3},,093000,160000,\n".format(symbol, self.timeFrame, self.startDate, self.endDate)
        message = "HIT,{0},{1},{2},{3},,{4},{5},1,TESTREQUEST,5000,'s'\n".format(symbol, self.timeFrame, self.startDate, self.endDate, self.beginFilterTime, self.endFilterTime)
        return message

    
    def get_message_interval(self, symbol):
        message = "HIT,{0},'{1}',{2},{3},,093000,160000,1\n".format(symbol, self.timeFrame, self.startDate, self.endDate)
        return message


    def get_message_daily(self, symbol):
        #message = "HIT,{0},'{1}',{2},{3},,093000,160000,1\n".format(symbol, self.timeFrame, self.startDate, self.endDate)
        #message = "HTD,[Symbol],[Days],[MaxDatapoints],[BeginFilterTime],[EndFilterTime],[DataDirection],[RequestID],[DatapointsPerSend]<CR><LF>"
        #HID,[Symbol],[Interval],[Days],[MaxDatapoints],[BeginFilterTime],[EndFilterTime],[DataDirection],[RequestID],[DatapointsPerSend],[IntervalType]<CR><LF> 
        message = "HDT,{0},{1},{2},,1,TESTREQUEST,2500\n".format(symbol, self.startDate[:8], self.endDate[:8])
        #message = "HDT,GOOG,20170619,20170830,,1,TESTREQUEST,2500\n"
        return message


    def reorder_ohlc(self, data):
        # REORDER the columns to OHLC (I think by default they come HLOC)
        lines = []
        for line in data.split("\n"):
            x = line.split(',')
            if len(x) == 8:
                if self.timeFrame == 0:
                    text = "{1},{2},{3},{4},{5},{6},{7}".format(x[0], x[1][:10], x[4], x[2], x[3], x[5], x[6], x[7])
                else:
                    text = "{1},{2},{3},{4},{5},{6},{7}".format(x[0], x[1], x[4], x[2], x[3], x[5], x[6], x[7])
                lines.append(text)
        return "\n".join(lines)


    def iqfeed_request(self, symbol):
        if self.timeFrame == 0:
            message = self.get_message_daily(symbol)
        else:
            message = self.get_message_minute(symbol)
        print(message)
        
        # Open a streaming socket to the IQFeed server locally
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        
        sock.sendall(message)
        data = self.read_historical_data_socket(sock)
        sock.close
        
        # Remove all the endlines and line-ending
        # comma delimiter from each record
        data = "".join(data.split("\r"))
        data = data.replace(",\n","\n")[:-1]
        
        return data
        
 
    def download_symbol(self, symbol, write_file=False):
        # Construct the message needed by IQFeed to retrieve data
        #[bars in seconds],[beginning date: CCYYMMDD HHmmSS],[ending date: CCYYMMDD HHmmSS],[empty],[beginning time filter: HHmmSS],[ending time filter: HHmmSS],[old or new: 0 or 1],[empty],[queue data points per second]
        #message = "HIT,%s,%i,%s,%s,,093000,160000,1\n" % symbol, self.timeFrame, self.startDate, self.endDate
        #message = message = "HIT,%s,%s,20150101 075000,,,093000,160000,1\n" % symbol, self.timeFrame

        if self.timeFrame == 0:    
            fileName = "{0}{1}-{2}-{3}-{4}.csv".format(self.downloadDir, symbol, "daily", self.startDate[:8], self.endDate[:8])
        else:
            fileName = "{0}{1}-{2}-{3}-{4}.csv".format(self.downloadDir, symbol, self.timeFrame, self.startDate[:8], self.endDate[:8])
        print(fileName)

        override = True
        exists = os.path.isfile(fileName)
        if exists == False or override == True:       
            data = self.iqfeed_request(symbol)
            # Write the data stream to disk

            #all_lines = "\n".join(lines)
            f = open(fileName, "w")
            f.write("DateTime,Open,High,Low,Close,Volume,OpenInterest\n")
            #f.write(data)
            f.write(self.reorder_ohlc(data))
            f.close()
            
        df = pd.io.parsers.read_csv(fileName, header=0, index_col=0, names=['DateTime','Open','High','Low','Close','Volume','oi'], parse_dates=True)
        df['Symbol'] = symbol
        if write_file == False:
            try:
                os.remove(fileName)
            except:
                print("Could not remove file")  # '{0}'".format(filename))
        return df
