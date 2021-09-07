myDict = {
    "fast": "In a quick Manner",
    "rahul": "A good boy",
    "marks": [1,2,5],
    "anotherdict": {'rahul': 'player'},
    1:2
}
print(list(myDict.keys())) # Print the keys of the dictionary
print(list(myDict.values())) # Prints the keys of the dictionary
print(list(myDict.items())) # Prints the (keys, value) for all contents of the dictionary
print(myDict)
updateDict = {
    "lovish": "friend",
    "Vipul": "friend",
    "Divya": "friend",
    "rahul": "A bad boy" # change or update the privius statement
}
myDict.update(updateDict) # Update the dictionary by adding key-value pairs from updateDict
print(myDict)

# The difference between .get and [] syntx in dictionaries
print(myDict.get("rahul2")) # Return None as rahul2 is not present in the dictionary
# print(myDict.["rahul2"]) # Throws an error as rahul2 is not present in the dictionary