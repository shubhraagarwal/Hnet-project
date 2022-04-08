const express = require("express");
const request = require("request");
const mongoose = require("mongoose");
const app = express();

const { MongoClient, ServerApiVersion } = require("mongodb");
const uri =
  "mongodb+srv://admin:admin@cluster0.wehxb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(
  uri,
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    serverApi: ServerApiVersion.v1,
  },
  (err) => {
    if (err) {
      console.log(err);
    }
  }
);

const PORT = 3100;

// async function run() {
//   try {
//     await client.connect();
//     console.log("first");
//     const database = client.db("Data");
//     const collection = database.collection("nodeOne");
//     // request(
//     //   "http://127.0.0.1:5100/sensor_data1",
//     //   function (error, response, body) {
//     //     // console.log(body);
//     //     collection.insertMany(body);
//     //   }
//     // );
//     collection.insertOne({ title: "hello" });
//   } finally {
//     // Ensures that the client will close when you finish/error
//     await client.close();
//   }
// }
// run().catch(console.dir);
// function getNodeData() {
app.get("/", async (req, res) => {
  await client.connect();
  console.log("first");
  const database = client.db("Data");
  const collection = database.collection("nodeOne");
  request(
    "http://127.0.0.1:5100/sensor_data1",
    async function (error, response, body) {
      // console.log(body);
      // collection.insertMany(body);
      // const ans = await collection.findOne({ title: "Hello" });
      // console.log(ans);
      console.log(typeof body);
      console.log(body);
      // collection.insertMany(body, function (err, result) {
      //   if (err) {
      //     res.status(400).send("Error inserting matches!");
      //   } else {
      //     console.log(`Added a new match with id ${result.insertedId}`);
      //     res.status(204).send();
      //   }
      // });
      res.send(body);
    }
  );
  // Ensures that the client will close when you finish/error
  console.log("inside finally");
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
// }

// setTimeout(getNodeData, 10000);

app.listen(PORT, function () {
  console.log("Listening on Port 3100");
});
