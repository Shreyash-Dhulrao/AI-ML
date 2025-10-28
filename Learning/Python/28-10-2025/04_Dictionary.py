a = {
    "name": "Shreyash",
    "age": 23,
    "edu": "Comp Engg"
}

print(a)
print(a["age"]) # We can print the value by using key value pair
print(a.keys()) # Here we get all the keys 
print(a.values()) # Here we get all the values
a.pop("age") # this helps to remove something by key value pair 
print(a)