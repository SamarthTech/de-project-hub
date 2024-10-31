class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append(Contact(name, phone))

    def display_contacts(self):
        for i, contact in enumerate(self.contacts):
            print(f"{i + 1}: {contact.name} - {contact.phone}")

def main():
    book = ContactBook()
    while True:
        action = input("Choose action (add, show, quit): ").strip().lower()
        if action == "add":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            book.add_contact(name, phone)
        elif action == "show":
            book.display_contacts()
        elif action == "quit":
            break
        else:
            print("Invalid action!")

if __name__ == "__main__":
    main()
