# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("all keys", thisDict.keys())
print("all values", thisDict.values())

# change items
# change value
thisDict["brand"] = "BMW"
print(thisDict["brand"])

# update dictionary
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisDict.update({"color": "red"})
print(thisDict)

# The pop() method removes the item with the specified key name:
thisDict.pop("color")
print(thisDict)

# The popitem() method removes the last inserted item
thisDict.popitem()
print(thisDict)

# looping

# Print all key names in the dictionary, one by one:
for key in thisDict.keys():
    print("key", key)

for value in thisDict.values():
    print("value", value)

for key, value in thisDict.items():
    print("key", key)
    print("value", value)


# copy dictionary

copyDict = dict(thisDict)
print("copyDict", copyDict)

# nested dictionary
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print("Family", myFamily["child1"]["name"])
