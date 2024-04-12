myfam = {  # it has key value pairs
    "ansh": "me",
    "arpita": "didi",
    "ashok": "papa",
    "nabanita": "mom",
    "no.": [4]
}
# we can make nested dictionary as well
# we cannot add the values we can only change them
print(myfam['no.'])

# Methods

print(myfam.keys())

print(myfam.values())

print(myfam.items())   # This can be used when an iteration is needed

myfam2 = {
    "we": "love each other"
}
myfam.update(myfam2)
print(myfam.items())

print(myfam.get("ansh2"))
# if this key is not present then it shows none in the output
# print(myfam["ansh"])    # where as this will show and error
