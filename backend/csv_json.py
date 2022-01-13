from flask import Flask, request
import json
import csv

app = Flask(__name__)


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
    f = open("sensor_data.json", "r")
    file_contents = f.read()
    return(file_contents)


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
