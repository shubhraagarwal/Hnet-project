import "./App.css";
import sensorData from "./Dummy Data/sensor_data.json";
import totalTraffic from "./Dummy Data/total_traffic.json";
import { Line } from "react-chartjs-2";

function App() {
  // useEffect(() => {
  //   axios.get("http://127.0.0.1:5100/sensor_data").then((res) => {
  //     setNodeOne(res.data.Node1);
  //     console.log(res.data);
  //   });
  // }, []);
  // const [nodeOne, setNodeOne] = useState();
  // const [nodeTwo, setNodeTwo] = useState();
  console.log(sensorData);
  return (
    <div className="App">
      {/* Line graph for sensor data */}
      <h1>Sensor Data</h1>
      <br />
      <h2>Node 1</h2>
      <h3>Humidity</h3>

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
          ],
          labels: sensorData.map((sensor) => {
            return sensor["Received Time"];
          }),
        }}
      />
      <h3>Temprature</h3>

      <Line
        data={{
          datasets: [
            {
              label: "Humidity",
              data: sensorData.map((sensor) => {
                return sensor.Temperature;
              }),
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 1,
            },
          ],
          labels: sensorData.map((sensor) => {
            return sensor["Received Time"];
          }),
        }}
      />
      <h3>Light</h3>

      <Line
        data={{
          datasets: [
            {
              label: "Humidity",
              data: sensorData.map((sensor) => {
                return sensor.Light;
              }),
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 1,
            },
          ],
          labels: sensorData.map((sensor) => {
            return sensor["Received Time"];
          }),
        }}
      />
      <h3>Sound</h3>

      <Line
        data={{
          datasets: [
            {
              label: "Humidity",
              data: sensorData.map((sensor) => {
                return sensor.Sound;
              }),
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 1,
            },
          ],
          labels: sensorData.map((sensor) => {
            return sensor["Received Time"];
          }),
        }}
      />
      <br />
      <h2>Node 2</h2>
      <h3>Humidity</h3>

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
          ],
          labels: sensorData.map((sensor) => {
            return sensor["Received Time"];
          }),
        }}
      />
      <h3>Temprature</h3>

      <Line
        data={{
          datasets: [
            {
              label: "Humidity",
              data: sensorData.map((sensor) => {
                return sensor.Temperature;
              }),
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 1,
            },
          ],
          labels: sensorData.map((sensor) => {
            return sensor["Received Time"];
          }),
        }}
      />
      <h3>Light</h3>

      <Line
        data={{
          datasets: [
            {
              label: "Humidity",
              data: sensorData.map((sensor) => {
                return sensor.Light;
              }),
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 1,
            },
          ],
          labels: sensorData.map((sensor) => {
            return sensor["Received Time"];
          }),
        }}
      />
      <h3>Sound</h3>

      <Line
        data={{
          datasets: [
            {
              label: "Humidity",
              data: sensorData.map((sensor) => {
                return sensor.Sound;
              }),
              backgroundColor: "rgba(255, 99, 132, 0.2)",
              borderColor: "rgba(255, 99, 132, 1)",
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
