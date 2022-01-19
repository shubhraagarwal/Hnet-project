from flask import Flask, request
import json
import csv
import pandas as pd
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

df_1 = pd.read_csv("Sensor Data.csv")
df_1 = df_1[df_1['Node ID'] == 1]
df_1.to_csv('Sensor Data 1.csv')

df_2 = pd.read_csv("Sensor Data.csv")
df_2 = df_2[df_2['Node ID'] == 2]
df_2.to_csv('Sensor Data 2.csv')


@app.route('/sensor_data', methods=['GET', 'POST'])
def sensor_data():
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
    with open("sensor_data.json", "w") as f:
        json.dump(data, f)
    f = open("sensor_data.json", "r")
    file_contents = f.read()

    with open("Sensor Data 2.csv", "r") as f1:
        reader = csv.reader(f1)
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
    with open("sensor_data.json", "w") as f1:
        json.dump(data, f1)
    f1 = open("sensor_data.json", "r")
    file1_contents = f1.read()

    return 'Node 1:{} \n Node 2:{}'.format(file_contents, file1_contents)


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
    app.run(debug=True, port=5100)
