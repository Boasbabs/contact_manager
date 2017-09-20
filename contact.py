# Class that models contact address

"""
Create a ContactManager that manages a list of Contacts
Create a loop that prompts to either add a contact, delete, or search for a contact by name
Commit Early + often

1. use a file to save contacts
2. when you restart the program it should read contacts from the file



REQUIREMENTS TO MEET
On GitHub,
- There is a git ignore/ no nonsense is committed
- Commit messages are readable
-  Commented out blocks of code are not in commits
Code is readable
- follows PEP8
- problem is broken into logical pieces
Code works
- Meets all the requirements of problem
"""


class Contact():

    # this class takes different parameters of a contact    input('Enter your name: ') input("Enter your phone number: ")
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        # self.gender = input("Enter your sex, M/F: ")
        # self.email = input("Enter your email address: ")
        # self.postal = input("Enter your postal address: ")
        self.contact=[]

    def build_details(self):
        self.contact.append(self.name)
        self.contact.append(self.phone_number)

    def __repr__(self):
        return '{}'.format(self.name)


class ContactManager:
    # the new contacts are assigned to a list
    def __init__(self, contact=[]):
       self.contacts = contact

    # this method returns all the details of contact
    def contact_details(self):
        print(self.contacts[contact.name])

    # this adds contacts to the list
    def add_contact(self, new_contact):                          a
        self.contacts.append(new_contact)

    # this deletes contacts from the list
    def remove_contact(self, contact):
        #if contact in contacts:
        #    self.contacts.remove(contact)
        #    return contact
        #return None
        pass


new_name = input("New name?: ")
new_number = input("New number?: ")

simeon = ContactManager(Contact(new_name, new_number))
print(simeon.contact_details())
# simeon.add_contact(Contact("pode", "3232"))
# simeon.Contact.get_details()






