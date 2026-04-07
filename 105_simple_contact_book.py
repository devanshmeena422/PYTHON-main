contacts = {}

n = int(input("How many contacts: "))

for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone

print("Contacts:", contacts)
