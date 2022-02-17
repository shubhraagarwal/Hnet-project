const express = require("express");
const request = require("request");

const app = express();

const { MongoClient, ServerApiVersion } = require("mongodb");
const uri =
  "mongodb+srv://admin:admin@cluster0.wehxb.mongodb.net/Cluster0?retryWrites=true&w=majority";
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  serverApi: ServerApiVersion.v1,
});

const PORT = 3100;

// function getNodeData() {
app.get("/", (req, res) => {
  client.connect((err) => {
    // perform actions on the collection object
    const collectionOne = client.db("Data").collection("nodeOne");

    request(
      "http://127.0.0.1:5100/sensor_data1",
      function (error, response, body) {
        console.error("error:", error); // Print the error
        console.log("statusCode:", response && response.statusCode); // Print the response status code if a response was received
        console.log("body:", body); // Print the data received
        collectionOne.insertOne(JSON.parse(body));
      }
    );
    res.send("data inserted");
    client.close();
  });
  // request(
  //   "http://127.0.0.1:5100/sensor_data2",
  //   function (error, response, body) {
  //     console.error("error:", error); // Print the error
  //     console.log("statusCode:", response && response.statusCode); // Print the response status code if a response was received
  //     console.log("body:", body); // Print the data received
  //     res.send(body); //Display the response on the website
  //   }
  // );
  // request(
  //   "http://127.0.0.1:5100/total_traffic",
  //   function (error, response, body) {
  //     console.error("error:", error); // Print the error
  //     console.log("statusCode:", response && response.statusCode); // Print the response status code if a response was received
  //     console.log("body:", body); // Print the data received
  //     res.send(body); //Display the response on the website
  //   }
  // );
});
// }

// setTimeout(getNodeData, 10000);

app.listen(PORT, function () {
  console.log("Listening on Port 3100");
});
