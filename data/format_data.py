import json
import matplotlib.pyplot as plt

f1 = open("data/data_cleansed.csv", "r")
lines = f1.readlines()

dictionary = {}

dictionary["borough"] = {}

for i in lines:
    aspwer = i.split(",")
    print(i.split(",")[2])
    if aspwer[2] in dictionary["borough"]:
        dictionary["borough"][aspwer[2]].append(aspwer)
    else:
        dictionary["borough"][aspwer[2]] = [i]
f1.close()

#Save the json object to a file
f2 = open("data/arrest_data.json", "w")
json.dump(dictionary, f2, indent = 4)