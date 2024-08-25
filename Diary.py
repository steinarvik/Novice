import datetime


def main():
    # Get today's date and format it as YYYY-MM-DD
    today = datetime.date.today()
    filename = f"{today}.txt"

    # Prompt the user to enter their notes
    print("Enter your notes for today. Type 'exit' to save and exit.")

    # Initialize an empty list to hold the notes
    notes = []

    # Read lines of input until the user types "exit"
    while True:
        line = input()
        if line == "exit":
            break
        notes.append(line)

    # Join all the notes into a single string
    content = "\n".join(notes)

    # Write the notes to the file named with today's date
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Your notes have been saved to {filename}")


if __name__ == "__main__":
    main()