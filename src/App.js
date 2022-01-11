import "./App.css";
import sensorData from "./Dummy Data/sensor_data.json";
import totalTraffic from "./Dummy Data/total_traffic.json";
import { Line } from "react-chartjs-2";

function App() {
  return (
    <div className="App">
      {/* Line graph for sensor data */}
      <h1>Sensor Data</h1>
      <Line
        data={{
          datasets: [
            {
              label: "Humidity",
              data: sensorData.map((sensor) => {
                return sensor.Humidity;
              }),
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 1,
            },
            {
              label: "Temperature",
              data: sensorData.map((sensor) => {
                return sensor.Temperature;
              }),
              backgroundColor: "rgba(163, 186, 37, 0.4)",
              borderColor: "rgba(163, 186, 37, 1)",
              borderWidth: 1,
            },
            {
              label: "Sound",
              data: sensorData.map((sensor) => {
                return sensor.Sound;
              }),
              backgroundColor: "rgba(37, 186, 134, 0.2)",
              borderColor: "rgba(37, 186, 134, 1)",
              borderWidth: 1,
            },
            {
              label: "Light",
              data: sensorData.map((sensor) => {
                return sensor.Light;
              }),
              backgroundColor: "rgba(60, 37, 186, 0.2)",
              borderColor: "rgba(60, 37, 186, 1)",
              borderWidth: 1,
            },
          ],
          labels: sensorData.map((sensor) => {
            return sensor["Received Time"];
          }),
        }}
      />
      {/* Line graph for total traffic */}
      <br />
      <hr />
      <h1>Total Traffic</h1>
      <Line
        data={{
          datasets: [
            {
              label: "Size",
              data: totalTraffic.map((traffic) => {
                console.log(traffic.Size);
                return traffic.Size.slice(0, 3);
              }),
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 1,
            },
          ],
          labels: totalTraffic.map((traffic) => {
            return traffic["Received Time"];
          }),
        }}
      />
    </div>
  );
}

export default App;
