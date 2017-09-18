# Class that models contact address

class ContactManager():

    # this class takes different parameters of a contact
    def __int__(self, name, ph_number, sex, email_address, postal_address):
        self.contact_name = name
        self.contact_ph_number = ph_number
        self.contact_sex = sex
        self.contact_email = email_address
        self.contact_address = postal_address

    # this method returns all the details of contact