"""
1. MEST is throwing a crazy networking party.
They need us to write software to register guests.
A. Take user input to store names and corresponding email in a dictionary
B. Given a name, output an email.
C. Send an email to all guest thanking them for showing
D. If the guest has an odd number of letters in their name
    send them a different email, telling them they are unwelcome at future events.
"""

"""
Create a class, that builds a dictionary
A search function for find name
"""

guest_list = {"simeon":"email"}


def add_guest():
    # condition to add new guest at least once
    new_addition = True
    # loop to continually add guest
    while new_addition:

        # get inputs of guests
        name = input("Guest Name?: ").lower()
        email = input("Guest Email?: ").lower()

        # build dictionary of guest
        guest_list[name] = email

        # ask for more guest
        ask_to_continue = input("More? Enter to continue or Q to quit").lower()

        if ask_to_continue == "q":
            new_addition = False


# function to search guest list
def search_guest():
    # get name to search from user
    search_keyword = input("Name to find?: ").lower()

    # condition to check if name is in dict.
    if search_keyword in guest_list.keys():
        return "{} is in the list and his/her email is {}".format(search_keyword.capitalize(), guest_list[search_keyword])
    else:
        return "No name found! As you sure of guest"


# function to guest with even letter
def even_letter_guest(name_letter):

    if len(name_letter) % 2 != 0:
        return False
    else:
        return True


print(even_letter_guest("simeon"))

