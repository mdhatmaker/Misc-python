import sys
import os
import requests
import re
from bs4 import BeautifulSoup
from PIL import Image
from os.path import join
from flask import Flask
from flask_restful import Resource, Api, reqparse


output_dir = "/Users/michael/Downloads/scrape"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)



def remove_list_duplicates(list):
   return [*set(list)]


def get_latest_index(url = "https://www.tradingview.com/markets/indices/quotes-all/"):
  rowList = []
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return
  soup = BeautifulSoup(response.text, 'html.parser')
  table = soup.find("table")  #, {"class": "table-Ngq2xrc6"})
  rows = table.find_all("tr", {"class": "listRow"}) #row-RdUXZpkv listRow"})
  for tr in rows:
    rowStr = ""
    cells = tr.find_all("td")
    firstCell = True
    for td in cells:
      if firstCell:
        img = td.find("img")
        #imgsrc = img['src']
        a = td.find("a")
        tickerName = a.text
        sup = td.find("sup")
        tickerDescription = sup.text
        #print(f"[{imgsrc}]  {tickerName}  {tickerDescription}", end=' | ')
        #print(f"{tickerName} | {tickerDescription}", end=' | ')
        rowStr += f"{tickerName} | {tickerDescription}"
        firstCell = False
      else:
        #print(f"{td.text}", end=' | ')
        rowStr += f" | {td.text}"
    #print()
    rowList.append(rowStr)
  return rowList



app = Flask(__name__)
api = Api(app)

STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}

parser = reqparse.RequestParser()

class StudentsList(Resource):
  def get(self):
    return STUDENTS
  def post(self):
    parser.add_argument("name")
    parser.add_argument("age")
    parser.add_argument("spec")
    args = parser.parse_args()
    student_id = int(max(STUDENTS.keys())) + 1
    student_id = '%i' % student_id
    STUDENTS[student_id] = {
      "name": args["name"],
      "age": args["age"],
      "spec": args["spec"],
    }
    return STUDENTS[student_id], 201    
   
api.add_resource(StudentsList, '/students/')


class IndexList(Resource):
  def get(self):
    rows = get_latest_index()
    return rows
    
api.add_resource(IndexList, '/indices/')



if __name__ == "__main__":
  app.run(debug=True)


#get_latest_index()
#sys.exit()
