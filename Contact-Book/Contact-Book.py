class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = Contact(name, phone, email, address)

    def view_contact_list(self):
        for name, contact in self.contacts.items():
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_str):
        for name, contact in self.contacts.items():
            if search_str.lower() in name.lower() or search_str.lower() in contact.phone.lower():
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            if address:
                self.contacts[name].address = address
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == 2:
            contact_book.view_contact_list()
        elif choice == 3:
            search_str = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_str)
        elif choice == 4:
            name = input("Enter name of contact to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            contact_book.update_contact(name, phone, email, address)
        elif choice == 5:
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()