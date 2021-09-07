# Write a program to accept marks of 6 students and display then in a sorted manner
m1 = int(input("Enter your marks: "))
m2 = int(input("Enter your marks: "))
m3 = int(input("Enter your marks: "))
m4 = int(input("Enter your marks: "))
m5 = int(input("Enter your marks: "))
m6 = int(input("Enter your marks: "))
myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)