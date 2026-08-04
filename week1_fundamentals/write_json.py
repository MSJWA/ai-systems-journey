import json

my_data = {"name": "Ali", "age": 21, "learning": "Python"}

with open("output.json", "w") as file:
    json.dump(my_data, file)