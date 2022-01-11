from flask import Flask, request
import json
import csv
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/sensor_data', methods=['GET', 'POST'])
def sensor_data():
    with open("Sensor Data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = []

        for row in reader:
            data.append({"Received Time": row[3],
                         "Temperature": row[5],
                         "Humidity": row[6],
                         "Light": row[7],
                         "Sound": row[8]
                         })
    with open("sensor_data.json", "w") as f:
        json.dump(data, f)
        return("CSV to JSON done")


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
        return("CSV to JSON done")


if __name__ == '__main__':
    app.run(debug=True, port=5100)
