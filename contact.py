# Class that models contact address

class ContactManager():

    # this class takes different parameters of a contact
    def __init__(self, name, ph_number, gender, email_address, postal_address):
        self.contact_name = name
        self.contact_ph_number = ph_number
        self.contact_sex = gender
        self.contact_email = email_address
        self.contact_address = postal_address

    # this method returns all the details of contact
    def contact_details(self):
        return 'Your Name is: {}'.format(self.contact_name)

name = input('Enter your name: ')
phone_number = input("Enter your phone number: ")
gender = input("Enter your sex, M/F: ")
email = input("Enter your email address: ")
postal = input("Enter your postal address: ")

# A new contact is created here
new_contact = ContactManager(name, phone_number, gender, email, postal)

print(new_contact.contact_details())
