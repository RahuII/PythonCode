# Write a program to create a dictionary of Hindi words with values as their english traslation provide user with an option to look it up!
engDic = {"achha": "good", "khush": "happy", "dukhi": "sad"}
print("Option are: ", engDic.keys())
a = input("Enter the hindi word.\n")
# print("The Emglish meaning of your word is: ",engDic[a])

# Below line will not throw an error if thhe key is not present in dictionary.

print("The Emglish meaning of your word is: ", engDic.get(a))
