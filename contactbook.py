class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}")
                print(f"   Phone: {contact.phone_number}")
                print(f"   Email: {contact.email}")
                print(f"   Address: {contact.address}")
                print()

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"{name} has been deleted from contacts.")
                return
        print(f"Contact with name {name} not found.")

    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"{name}'s contact information updated successfully.")
                return
        print(f"Contact with name {name} not found.")

# Example usage
contact_book = ContactBook()

while True:
    print("\n1> Add Contact")
    print("2> Display Contacts")
    print("3> Delete Contact")
    print("4> Update Contact")
    print("5> Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        contact_book.add_contact(contact)

    elif choice == '2':
        contact_book.display_contacts()

    elif choice == '3':
        name = input("Enter name to delete: ")
        contact_book.delete_contact(name)

    elif choice == '4':
        name = input("Enter name to update: ")
        new_phone_number = input("Enter new phone number (leave empty to skip): ")
        new_email = input("Enter new email (leave empty to skip): ")
        new_address = input("Enter new address (leave empty to skip): ")
        contact_book.update_contact(name, new_phone_number, new_email, new_address)

    elif choice == '5':
        print("Exiting...!!!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
