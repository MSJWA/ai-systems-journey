import json

my_data = {"hobbies": "Mostly for physical part is tennis alongwith jogging", "interest" : "doing photography whereever seems feasible", "impact" : "would love to excel around in AI learn a bit more about cybersecurity especially the blockchaining side of that"}

with open("facts.json", "w") as file:
    json.dump(my_data, file)