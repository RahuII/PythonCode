greeting = "Good morning, "
name = "Rahul"
print(type(name))

        # Concatenating two strings
c = greeting + name
print(c)

name = "Rahul"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# name[3] = "d"         --> Does not work

        # string sliceing
print(name[0:4])       # it will print 0 to 3rd letter or 4 one is ignor.
print(name[:4])        # is same as name[0:4] it's takes atomatic initial point.
print(name[0:])        # is same as name[0:5] it's takes atomatic last point.
print(name[-1])        # it's print last one letter.
print(name[-2])        # it's also print second last letter.
print(name[-4:-1])     # it's same as name[1:4]
        # slicing with skip value
name = "Rahulisagoodboy"
print(name[1:4:1]) 
print(name[::2]) # print every secound number at the end
