#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process
from flask import Flask, render_template, request, send_from_directory
from flaskwebgui import FlaskUI #get the FlaskUI class  
import pandas as pd
from flask import request, jsonify
import random
import string    
import csv
import os
from flask import send_file


#from pyfladesk import init_gui


app = Flask(__name__)
# Feed it the flask app instance 
ui = FlaskUI(app)

# do your logic as usual in Flask

@app.route('/api/v1/resources/generate', methods=['POST',"GET"])
def apigenerate():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
   
    S = 10    
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    result=[random.randint(2,20),str(ran),random.uniform(1.5, 1.9),''.join(random.choice('0123456789ABCDEF') for i in range(16))]

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    with open('report.csv','a+',encoding="utf-8", newline='') as csv_file:
                                    writer = csv.writer(csv_file,lineterminator='\n')
                                    writer.writerows([result],)
    return jsonify(result)

@app.route('/api/v1/resources/download', methods=['POST',"GET"])
def adownloadFile():
  
   
     
    result=os.path.basename("C:\\Users\\User\\Desktop\\my-app>\\report.csv")
    return send_file(result, as_attachment=True)
@app.route('/api/v1/resources/getReport', methods=['POST',"GET"])
def getRepoert():
  
   
    file = open("report.csv")
    numline = len(file.readlines())
    return jsonify(numline)


# call the 'run' method
#ui.run()

if __name__ == '__main__':
   app.run()


# if __name__ == '__main__':
#     init_gui(app, port=5000, width=1980, height=1280,
#              window_title="PyFladesk", argv=None)
