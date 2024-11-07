import random
import string

# Step 1: Generate a random string of 10 characters
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Step 2: Define the file name using the random string
file_name = f"{random_string}.txt"

# Step 3: Create and open the file in write mode
with open(file_name, "w") as file:
    # Step 4: Write the random string inside the file
    file.write(random_string)

# Step 5: Print a success message
print(f"File '{file_name}' has been created with the content: {random_string}")
