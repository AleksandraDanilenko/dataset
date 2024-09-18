# Reading Exported MongoDB Data in Python and JavaScript

This guide demonstrates how to read MongoDB data exported in both JSON and BSON formats using Python and JavaScript. The data files (`users.json` and `users.bson`) should be located in the same folder as your script.

## 0. Link to User Database
https://disk.yandex.ru/d/pAdHr76veHUs7g


## 1. Python Examples

### Reading from `users.json` in Python

To read data from `users.json`, you can use the built-in `json` module in Python.

```python
import json
import random
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the users.json file
json_file_path = os.path.join(script_dir, 'users.json')

# Load JSON data from the file
with open(json_file_path, 'r') as f:
    users = json.load(f)

# Get a random user
random_user = random.choice(users)

print("Random User:", random_user)
```

#### Explanation:

- The JSON file is loaded into a Python list using `json.load()`.
- A random user is selected from the list using `random.choice()`.

### Reading from `users.bson` in Python

To read BSON data, you'll need to install the `pymongo` library, which provides BSON decoding.

First, install the library:

```bash
pip install pymongo
```

Then, use the following code to read from the BSON file:

```python
from bson import decode_all
import random
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the users.bson file
bson_file_path = os.path.join(script_dir, 'users.bson')

# Read the BSON data from the file
with open(bson_file_path, 'rb') as f:
    users_data = f.read()

# Decode the BSON data
users = decode_all(users_data)

# Get a random user
random_user = random.choice(users)

print("Random User:", random_user)
```

#### Explanation:

- The BSON data is read from the file in binary mode.
- `decode_all()` from the `bson` module is used to decode all BSON documents into a list.
- A random user is selected similarly to the JSON example.

## 2. JavaScript Examples

### Reading from `users.json` in JavaScript (Node.js)

Node.js has a built-in `fs` (file system) module that you can use to read the JSON file.

First, make sure you have Node.js installed. Then, create a JavaScript file, e.g., `readUsers.js`:

```javascript
const fs = require("fs");
const path = require("path");

// Get the full path to the users.json file
const jsonFilePath = path.join(__dirname, "users.json");

// Read the JSON file
fs.readFile(jsonFilePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  // Parse the JSON data
  const users = JSON.parse(data);

  // Get a random user
  const randomUser = users[Math.floor(Math.random() * users.length)];

  console.log("Random User:", randomUser);
});
```

#### Explanation:

- `fs.readFile()` reads the JSON file asynchronously.
- `JSON.parse()` converts the JSON string into a JavaScript array.
- A random user is selected using a random index.

Run the script in the terminal:

```bash
node readUsers.js
```

### Reading from `users.bson` in JavaScript (Node.js)

To read BSON files in JavaScript, you need to install the `bson` package.

First, install the package:

```bash
npm install bson
```

Then, create a JavaScript file, e.g., `readUsersBson.js`:

```javascript
const fs = require("fs");
const path = require("path");
const BSON = require("bson");

// Get the full path to the users.bson file
const bsonFilePath = path.join(__dirname, "users.bson");

// Read the BSON file
fs.readFile(bsonFilePath, (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  // Decode the BSON data
  const users = BSON.deserialize(data);

  // Get a random user
  const randomUser = users[Math.floor(Math.random() * users.length)];

  console.log("Random User:", randomUser);
});
```

#### Explanation:

- `fs.readFile()` reads the BSON file in binary mode.
- `BSON.deserialize()` is used to parse the BSON data into a JavaScript array.
- A random user is selected in the same way as before.

Run the script:

```bash
node readUsersBson.js
```

## Summary

- **Python**: Use `json` for JSON and `pymongo` for BSON.
- **JavaScript**: Use Node.js `fs` module for file handling, and `JSON.parse` for JSON or `bson` package for BSON.

These examples demonstrate how to read and parse your MongoDB data in both Python and JavaScript environments. Let me know if you need any more help or further examples!

The dumped files can be easily shared or restored into another MongoDB instance using the `mongoimport` or `mongorestore` commands.
