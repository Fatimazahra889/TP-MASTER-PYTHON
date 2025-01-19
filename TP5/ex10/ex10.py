import csv
import os
import pandas as pd

cssv='TP5/ex10/contacts.csv'
def add_contacts():
    name=input('Name:')
    phone=input('Phone:')
    with open(cssv,'a',newline='')as f:
        writer=csv.writer(f)
        writer.writerow([name,phone])
    print("contact added successfully")

def list_contacts():
    with open(cssv,'r',newline='')as f:
        reader=csv.reader(f)
        for row in reader:
            print(f"Name: {row[0]},Phone: {row[1]}")

def search_contacts():
    name=input('enter the name that you want to search for:')
    with open(cssv,'r',newline='')as f:
        reader=csv.reader(f)
        for row in reader:
            if name in row:
                print(f"Name: {row[0]}, Phone: {row[1]}")
                return
        print("contact not found")
        search_contacts()

def delete_contacts():
    name = input("Enter the name you'd like to delete: ")
    found = False
    with open(cssv, 'r', newline='') as f:
        rows = list(csv.reader(f))
    with open(cssv, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            if row and row[0] != name:  
                writer.writerow(row)
            else:
                found = True
    if found:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("1. Add contact")
        print("2. list contacts")
        print("3. Search a contact by name")
        print("4. Delete a contact")
        print("5. Exit")

        choice =input("choose an option:")
        if choice=='1':
            add_contacts()
        elif choice=='2':
            list_contacts()
        elif choice=='3':
            search_contacts()
        elif choice=='4':
            delete_contacts()
        elif choice=='5':
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()
        


