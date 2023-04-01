dic = {"ansh": "firstname",
       "mondal": "lastname",
       "age": 21}
# it has key value pairs and we can create maping with it
print(dic["ansh"])

print(dic["age"])
print(dic.get("age"))

# these both gives the same output but get does not gives an error if there is no such value is present
print(dic.values())
print(dic.keys())

print(dic.items())
for key, value in dic.items():
    # f string should be used to get the variables of key and values in the string
    print(f"the value to the corresponding key {key} is {value}")

# DICTIONARY METHODS

dic2 = {"year": "third",
        "gender": "male"}

dic.update(dic2)
# dic.clear()  to clear the dictionary
dic.pop("age")
dic.popitem()  # removes the last item from the dictionary

print(dic)
del (dic)  # deletes the dictionary
edic = {}  # this is how an empty dictionary is created
