b = set()
print(type(b))
b.add(3)
b.add(7)
b.add(7)  # Adding a value repetedly does not change a set
b.add(6)
b.add(4)
b.add((4, 5, 3))
# b.add({4,6,3,2}) # we can't add list or dictionary to set.
print(b)
## Accesing element
print(len(b))  # Print the lenght of this set.

b.remove(7)  # Remove 7 from set.
# b.remove(15)  # Throing an error while trying to remove 15 which is not present in a set.
print(b)