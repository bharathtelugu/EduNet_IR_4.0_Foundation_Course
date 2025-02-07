import mysql.connector as mysql
from addingContact import addContact
from viewdata import viewContacts
from searchingContact import searchContact
from updatingContact import updateContact
from deletingContact import deleteContact

def main():
    while True:
        print("\nPersonal Contact Management System")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact by name")
        print("4. Update a contact's details")
        print("5. Delete a contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phoneNo = input("Enter phone: ")
            email = input("Enter email: ")
            addContact(name, phoneNo, email)
        elif choice == '2':
            viewContacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            searchContact(name)
        elif choice == '4':
            id = input("Enter contact ID to update: ")
            name = input("Enter new name: ")
            phoneNo= input("Enter new phone: ")
            email = input("Enter new email: ")
            updateContact(id, name, phoneNo, email)
        elif choice == '5':
            id = input("Enter contact ID to delete: ")
            deleteContact(id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()