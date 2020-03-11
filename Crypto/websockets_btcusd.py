import websocket
import ast
import json
import sqlite3

class DataFeed():

    def __init__(self):
        #create database
        file = "myDB.db"
        self.path = "/Users/michael/Dropbox/dev/PROJECTS/python-projects/data/"+file
        self.db = sqlite3.connect(self.path)
        self.cursor = self.db.cursor()
        self.cursor.execute(
            """CREATE TABLE ok_btcusd_depth(
            bid REAL,
            bid_amount REAL,
            ask REAL,
            ask_amount REAL)
            """)
        self.cursor.execute(
            """CREATE TABLE ok_btcusd_trades(
               price REAL,
               amount REAL,
               time TEXT,
               type TEXT)
               """)
        self.db.commit()
        #connect to websocket
        url = "wss://real.okcoin.com:10440/websocket/okcoinapi"
        self.ws = websocket.WebSocketApp(url,
                                         on_message=self.on_message,
                                         on_error=self.on_error
                                         )
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_message(self,ws,msg):
        msg = ast.literal_eval(msg) #convert string to list
        table = msg[0]["channel"]
        data = msg[0]["data"]
        if table == "ok_btcusd_depth":
            bid_info = data["bids"][0]
            ask_info = data["asks"][0]
            Tuple = (bid_info[0],bid_info[1],ask_info[0],ask_info[1])
            self.cursor.execute(
                """INSERT INTO ok_btcusd_depth(
                   bid,bid_amount,ask,ask_amount)
                   VALUES(?,?,?,?)""",Tuple )
        else:
            for trade in data:
                Tuple = (float(trade[0]),float(trade[1]),trade[2],trade[3])
                self.cursor.execute(
                    """INSERT INTO ok_btcusd_trades(price,amount,time,type)
                       VALUES(?,?,?,?)""",Tuple) 
        self.db.commit()

    def on_error(self,ws,error):
        print(error)

    def on_open(self,ws):
        request = [{"event":"addChannel","channel":"ok_btcusd_depth"},
                   {"event":"addChannel","channel":"ok_btcusd_trades"}]
        request = json.dumps(request)
        request = request.encode("utf-8")
        ws.send(request)

if __name__ == "__main__":
    DataFeed()
