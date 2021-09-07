# What will be the lenght of following set s s = set(), s.add(20), s.add(20.0), s.add("20")
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s) # Python was identify 20.0 as a int not a flaot.