mylist = ['a', 'b', 'c']

# Creating an empty list to store the tuples
indexed_list = []

# Using a for loop to iterate over the list with enumeration
for idx, item in enumerate(mylist):
    # Appending the tuple (item, index) to the indexed_list
    indexed_list.append((item, idx))

# Printing the original list and the indexed list
print("Indexed list:", indexed_list)

mylist = ['a', 'b', 'c', 'e', 'f']

# Using list comprehension to create a new list of tuples (element, index)
indexed_list = [(item, idx) for idx, item in enumerate(mylist)]

# Printing the original list and the indexed list
print("Indexed list:", indexed_list)