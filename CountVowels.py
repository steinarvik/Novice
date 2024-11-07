# Step 1: Define a string
text = "Hello, how many vowels are in this sentence?"

# Step 2: Define a variable to count vowels
vowel_count = 0

# Step 3: Loop through the string and check if each character is a vowel
for char in text.lower():  # Convert the string to lowercase for easier comparison
    if char in "aeiou":
        vowel_count += 1

# Step 4: Display the result
print(f"The number of vowels in the string is: {vowel_count}")
