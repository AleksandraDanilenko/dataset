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
