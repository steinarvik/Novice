# Step 1: Get user input
text = input("Enter a block of text for analysis:\n")

# Step 2: Initialize counters and storage
character_count = len(text)
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')
word_frequency = {}

# Step 3: Define a function to remove punctuation
def remove_punctuation(s):
    # Define a list of punctuation characters to remove
    punctuation = ".,!?:;'\"()[]{}"
    # Remove punctuation by replacing it with an empty string
    for char in punctuation:
        s = s.replace(char, "")
    return s

# Step 4: Analyze the text
# Remove punctuation and convert text to lowercase
cleaned_text = remove_punctuation(text).lower()
words = cleaned_text.split()

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Step 5: Calculate additional statistics
if word_count > 0:  # Avoid division by zero
    most_frequent_word = max(word_frequency, key=word_frequency.get)
    average_word_length = sum(len(word) for word in words) / word_count
    average_sentence_length = word_count / sentence_count if sentence_count > 0 else word_count
else:
    most_frequent_word = None
    average_word_length = 0
    average_sentence_length = 0

# Step 6: Display the results
print("\nText Analysis Results:")
print("-" * 22)
print(f"Total Characters: {character_count}")
print(f"Total Words: {word_count}")
print(f"Total Sentences: {sentence_count}")

if most_frequent_word:
    print(f"Most Frequent Word: '{most_frequent_word}' (used {word_frequency[most_frequent_word]} times)")

print(f"Average Word Length: {average_word_length:.2f} characters")
print(f"Average Sentence Length: {average_sentence_length:.2f} words")
