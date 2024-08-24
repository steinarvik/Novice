
# Get the user's full name
full_name = input("Please enter your full name: ")

# Display the name in uppercase
print("Your name in uppercase:", full_name.upper())

# Display the name in lowercase
print("Your name in lowercase:", full_name.lower())

# Remove spaces and count the total number of characters
name_no_spaces = full_name.replace(" ", "")
print(name_no_spaces)
print("Total number of characters (excluding spaces):", len(name_no_spaces))

# Reverse the name
reversed_name = full_name[::-1]
print("Your name reversed:", reversed_name)
