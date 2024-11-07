# Initialize an empty list to store the bilingual vocabulary
bilingual_vocabulary = []

# Start a while loop to continually prompt the user for input
while True:
    # Ask the user to enter a word in the first language (Language 1)
    word_lang1 = input("Enter a word in Language 1 (or type 'done' to finish): ").strip()

    # Check if the user wants to stop adding words
    if word_lang1.lower() == 'done':
        break

    # Ask the user to enter the translation in the second language (Language 2)
    translation_lang2 = input(f"Enter the translation of '{word_lang1}' in Language 2: ").strip()

    # Add the word and its translation to the list as a tuple
    bilingual_vocabulary.append((word_lang1, translation_lang2))

    # Confirm that the word was added
    print(f"'{word_lang1}' (Language 1) has been added with the translation: '{translation_lang2}' (Language 2)\n")

# Saving the list to a text file
with open('bilingual_vocabulary.txt', mode='w') as file:
    file.write("Language 1 - Language 2\n")  # Write the header
    for word_lang1, translation_lang2 in bilingual_vocabulary:
        file.write(f"{word_lang1} - {translation_lang2}\n")  # Write each word and its translation

# Print out the final list of bilingual vocabulary words
print("\nYour Bilingual Vocabulary List:")
for word_lang1, translation_lang2 in bilingual_vocabulary:
    print(f"{word_lang1} (Language 1): {translation_lang2} (Language 2)")

print("\nThe vocabulary has been saved to 'bilingual_vocabulary.txt'.")