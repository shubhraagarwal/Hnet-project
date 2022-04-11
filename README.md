# HNET

A brief description of what this project does and who it's for

## Python

```bash
cd backend
pip install requirements.txt
```

## Node

```
cd node
npm install
```

## Working with the API

You will need to have ngrok installed and setup in your local environment to get the API
up and running.

If you do not have ngrok already installed, you can follow the steps given <a href="https://ngrok.com/download"> here </a>

After setting up ngrok in your local environment, follow the steps given below

```
cd backend
python csv_json.py
```

After running the python script, you will be shown a link which NGROK has generated as a public endpoint for your localhost server.
Copy the URL and enter the following commands in your terminal.

```
cd ..
cd node
code index.js
```

These series of commands will open the node file in your text editor.

Paste the link you just copied from the terminal into line number `5` of the `index.js` file.

After this all you have to do is run `nodemon index.js` in your terminal and Voila! The API is up and running.

## Pushing data into the database

#### Push Sensor 1 Data into the database from the local python server

```http
  GET /one
```

To update the database with the latest readings from node `1`, hit the given endpoint once and wait for a 200 OK response.

#### Push Sensor 2 Data into the Database from the local python server

```http
  GET /two
```

To update the database with the latest readings from node `2`, hit the given endpoint once and wait for a 200 OK response.

#### Push Total Traffic Data into the Database from the local python server

```http
  GET /total_traffic
```

To update the database with the latest readings of traffic on the nodes, hit the given endpoint once and wait for a 200 OK response.

## Getting data from the database

### Get readings of node 1

```http
  GET /getnodeone
```

Returns an array of objects containing all the readings from node `1`.

### Get readings of node 2

```http
  GET /getnodetwo
```

Returns an array of objects containing all the readings from node `2`.

### Get readings of total traffic

```http
  GET /gettotaltraffic
```

Returns an array of objects containing all the readings about the total traffic on the node.
