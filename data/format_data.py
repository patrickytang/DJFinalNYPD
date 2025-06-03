import json
import matplotlib.pyplot as plt

f1 = open("data/data_cleansed.csv", "r")
lines = f1.readlines()

dictionary = {}
dict2 = {}
for i in lines:
    blank = i.split(",")
    if blank[1] in dict2:
        dict2[blank[1]] +=1
    else:
        dict2[blank[1]] = 1
    if blank[2] in dictionary:
        dictionary[blank[2]].append(blank)
    else:
        dictionary[blank[2]] = [blank]
    
print(dict2)


f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 1)