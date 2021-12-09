from flask import Flask, render_template, request
import pickle
import numpy as np
# from numpy.core.numeric import outer
# import jsonify
import requests
import sklearn
import pandas as pd
import cx_Oracle
import pickle
import platform
import os

app = Flask(__name__)

model = pickle.load(open('FSP_MODEL.pkl', 'rb'))

#cx_Oracle.init_oracle_client("/""Oracle database\instantclient_21_3")
#cx_Oracle.init_oracle_client(r"/home/jupterbrothersds/Check/instantclient_21_4")



#connection = cx_Oracle.connect(user="ADMIN",password="Innowell123@",dsn="tcps://adb.ap-mumbai-1.oraclecloud.com:1522/g74b61b42c68a40_litmusdata_high.adb.oraclecloud.com?wallet_location=admin/")

print("Successfully connected to Oracle Database")

@app.route("/", methods = ["GET","POST"])
def predict():
    prediction = model.predict([[1,2,3,4,5,6,7,8,9,10]])
    print(prediction)         
    return render_template('predict.html', pred=prediction)
    
if __name__ == '__main__':
    app.run(debug='true')
