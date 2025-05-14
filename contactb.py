class ContactBook:
    def __init__(self):
        self.allcontact = {}

    def DisplayContact(self):
        if not self.allcontact:
            print("Contact list is empty.\n")
            return
        print("\nAll Contacts:")
        for name, phone in self.allcontact.items():
            print(f"Name: {name}, Phone: {phone}")
        print()

    def AddContact(self):
        name = input("Enter the name of the person: ")
        phone = input("Enter the phone number of the person: ")
        self.allcontact[name] = phone
        print(f"Contact '{name}' added successfully.\n")

    def SearchContact(self):
        name = input("Enter the name of the contact to search: ")
        if name not in self.allcontact:
            print("Contact not available.\n")
        else:
            print(f"Found Contact: Name: {name}, Phone: {self.allcontact[name]}\n")

    def deleteContact(self):
        name = input("Enter the name of the contact you want to delete: ")
        if name in self.allcontact:
            del self.allcontact[name]
            print(f"Contact '{name}' deleted successfully.\n")
        else:
            print("Contact not available.\n")


# Main loop
obj = ContactBook()

while True:
    print("What do you want to do?")
    print("1. Display all contact list")
    print("2. Add a contact")
    print("3. Delete a contact")
    print("4. Search a contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        obj.DisplayContact()
    elif choice == '2':
        obj.AddContact()
    elif choice == '3':
        obj.deleteContact()
    elif choice == '4':
        obj.SearchContact()
    elif choice == '5':
        print("Thank you for using the Contact Book.")
        break
    else:
        print("Invalid entry. Please choose between 1 and 5.\n")
