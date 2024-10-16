

dic = {"a":1, "b":2, "c":3}

print(dic)
print(type(dic))

print(dic.keys())
print(dic.values())

# Replace an item
dic["a"] = 11
print(dic)

# Add an item
dic["d"] = 4
print(dic)

# Change an item
dic["a"] = 0
print(dic)

# Update an item
dic.update({"a":1})
print(dic)

# Pop an item
dic.pop("d")
print(dic)

# Delete an item
del dic["c"]
print(dic)

# Make a dictionary in a dictionary
dic["c"] = {"a":1, "b":2}
print(dic)

# Create empty dictionary
dic2 = {}
print(dic2)
# print(type(dic2))


dic3 = dic2
print(dic3)

# Summary:
# A dictionary is defined with curly braces {}.
# Keys are on the left of the colon, and values are on the right.
# Access a value by referring to its key using square brackets.