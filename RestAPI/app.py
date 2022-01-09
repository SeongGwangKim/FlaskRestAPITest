import requests
import json
from flask import Flask, jsonify, request
from s3_connection import s3_connection
import pandas as pd
import boto3
import io


# create app
app = Flask(__name__, static_folder='static')



# routes
@app.route('/square/', methods=['POST'])
def square():
    # get data
    data = request.get_json()[0]
    print(data)
    num_list = data.values()
    print(type(data))
    print(data["0"])
    print(data.values())
    print(type(num_list))
    print(num_list)
    response = {'results': data["0"]+'success'}
    # for n in num_list:
    #     square = n ** 2


    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
