# Write a program to fill in a letter template given below with name and date
letter = '''Dear <|NAME|>
Greeting from ABC coding house. I am happy to tell tell about your selection
You are selected!
Have a great day ahead!
Thanks and regards

Date: <|DATE|>'''
name = input("Enter your name:\n")
date = input("Enter date:\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)