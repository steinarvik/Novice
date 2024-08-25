import re

# Get text from text.txt file
# regex
with open('text.txt', 'r') as f:
    text = f.read()

# Regular expression patterns
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
phone_pattern = r'\(?\d{3}\)?[-.]\d{3}[-.]\d{4}|\d{3}-\d{3}-\d{4}'

# Finding matches
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

# Output
print(emails)
print(phones)