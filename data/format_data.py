import json
import matplotlib.pyplot as plt

f1 = open("data/data_cleansed.csv", "r")
lines = f1.readlines()

dictionary = {}

dictionary["borough"] = {}

dict2 = {}
for i in lines[1:]:
    aspwer = i.split(",")


    if aspwer[2] in dictionary["borough"]:
        if aspwer[1] in dictionary["borough"][aspwer[2]]:
            dictionary["borough"][aspwer[2]][aspwer[1]] += 1
        else:
            dictionary["borough"][aspwer[2]][aspwer[1]] = 1
    else:
        dictionary["borough"][aspwer[2]] = {}
        dictionary["borough"][aspwer[2]][aspwer[1]] = 1

for i in dictionary["borough"]:
    newlist = []
    total = 0

    for a in dictionary["borough"][i]:
        total+=dictionary["borough"][i][a]
        newlist.append([a,dictionary["borough"][i][a]])
    newlist.append(["total",total])
    dict2[i] = sorted(newlist,key=lambda x: x[1],reverse=True)




dict2["total"] = dict2["M"][0][1]+dict2["Q"][0][1]+dict2["B"][0][1]+dict2["K"][0][1]+dict2["S"][0][1]
newlist = []
for i in dict2["K"]:
    if i[0] != "total":
        newlist.append(i)
for i in dict2["M"]:
    true = True
    for a in range(len(newlist)):
        print(newlist[a][0])
        if i[0] == newlist[a][0]:
            true = False
            newlist[a][1] += i[1]
            break

for i in dict2["Q"]:
    true = True
    for a in range(len(newlist)):
        print(newlist[a][0])
        if i[0] == newlist[a][0]:
            true = False
            newlist[a][1] += i[1]
            break

for i in dict2["B"]:
    true = True
    for a in range(len(newlist)):
        print(newlist[a][0])
        if i[0] == newlist[a][0]:
            true = False
            newlist[a][1] += i[1]
            break

for i in dict2["S"]:
    true = True
    for a in range(len(newlist)):
        print(newlist[a][0])
        if i[0] == newlist[a][0]:
            true = False
            newlist[a][1] += i[1]
            break

print(newlist)
# print(newlist)
dict2["T"] = sorted(newlist,key=lambda x: x[1],reverse=True)
dict2["indiv"] = dictionary
f1.close()

#Save the json object to a file
f2 = open("data/arrest_data.json", "w")
json.dump(dict2, f2, indent = 4)
