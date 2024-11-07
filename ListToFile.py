# Simple Contact List Manager


contacts = []

while True:
    # Prompt for contact name
    name = input("Enter contact name (or type 'done' to finish): ").strip()

    if name.lower() == 'done':
        break

    # Prompt for contact phone number
    phone_number = input(f"Enter phone number for {name}: ").strip()

    # Add the contact to the list
    contacts.append(f"{name}: {phone_number}")

# Write the contacts to a text file
with open("contacts.txt", "w") as file:
    for contact in contacts:
        file.write(contact + "\n")

print("Contacts saved to 'contacts.txt'.")