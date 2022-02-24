from flask import Flask, request
import json
import csv
import pandas as pd
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
async_mode = None
app = Flask(__name__)
socket_ = SocketIO(app, async_mode=async_mode)
CORS(app, support_credentials=True)

df_1 = pd.read_csv("Sensor Data.csv", nrows=20)
df_1 = df_1[df_1['Node ID'] == 1]
df_1.to_csv('Sensor Data 1.csv')

df_2 = pd.read_csv("Sensor Data.csv", nrows=20)
df_2 = df_2[df_2['Node ID'] == 2]
df_2.to_csv('Sensor Data 2.csv')

# Sensor data for node 1


@app.route('/sensor_data1', methods=['GET', 'POST'])
def sensor_data1():
    with open("Sensor Data 1.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = []

        for row in reader:
            data.append({  # "Node ID": row[5],
                "Received Time": row[4],
                "Temperature": row[6],
                "Humidity": row[7],
                "Light": row[8],
                "Sound": row[9]
            })
    with open("sensor_data1.json", "w") as f:
        json.dump(data, f)
    f = open("sensor_data1.json", "r")
    file_contents = f.read()
    return (file_contents)

# Sensor data for node 2


@app.route('/sensor_data2', methods=['GET', 'POST'])
def sensor_data2():
    with open("Sensor Data 2.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = []

        for row in reader:
            data.append({  # "Node ID": row[5],
                "Received Time": row[4],
                "Temperature": row[6],
                "Humidity": row[7],
                "Light": row[8],
                "Sound": row[9]
            })
    with open("sensor_data2.json", "w") as f:
        json.dump(data, f)
    f = open("sensor_data2.json", "r")
    file_contents = f.read()
    return (file_contents)


@app.route('/total_traffic', methods=['GET', 'POST'])
def total_traffic():
    with open("Sensor Data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = []

        for row in reader:
            data.append({"Received Time": row[3],
                         "Size": row[11],
                         })
    with open("total_traffic.json", "w") as f:
        json.dump(data, f)
    f = open("total_traffic.json", "r")
    file_contents = f.read()
    return(file_contents)


if __name__ == '__main__':
    socket_.run(app, debug=True, port=5100)
