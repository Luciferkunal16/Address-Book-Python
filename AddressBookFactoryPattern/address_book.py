import logging

from AddressBookFactoryPattern.address_book_interface import AddressBookInterface
from AddressBookFactoryPattern.contact import Contact

logging.basicConfig(filename="address_book_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class AddressBook(AddressBookInterface):

    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.list_of_contact = dict()

    def add_person(self):
        """
        use to add persn to the list by inputing details of person details
        :return:updated list of contact
        """
        try:
            first_name = input("Enter the First name=")
            if first_name in self.list_of_contact.keys():
                print("Contact Already Exist!!! No Duplicate Contact Allowed ")
            else:
                last_name = input("Enter the Last name=")
                city = input("Enter the City=")
                state = input("Enter the State=")
                zip = input("Enter the zip code=")
                phone_number = input("Enter the Phone Number=")
                email = input("Enter the Email Address=")
                detail_obj = {"first_name": first_name, "last_name": last_name, "city": city, "state": state,
                              "zip": zip, "phone_number": phone_number, "email": email}

                person = Contact(detail_obj)
                self.list_of_contact.update({first_name: person})

                return self.list_of_contact.values()
        except Exception as e:
            print(e)
            self.logger.error("Error is {} ".format(e))
            self.logger.info()

    def display_all_contact(self):
        """
        Print list of contact available i list
        :return:
        """
        if bool(self.list_of_contact):
            print("Address Book is")
            for values in self.list_of_contact.values():
                print(values.get_all_details())

        else:
            print("Address book is Empty")

    def delete_contact(self):
        """

        :param f_name: First Name of Contact person
        :return:True if Delete Successfull and False if Unsuccessfull
        """
        try:

            f_name = input("Enter the First Name of whose Contact you wan to delete")
            if f_name in self.list_of_contact.keys():
                self.list_of_contact.pop(f_name)
                print("Contact is Deleted!!!!!!!")
                return True
            else:
                print("Contact Not Exist")
                return False
        except Exception as err:
            logging.error(err)
            print(err)

    def edit_contact(self):
        """
        for Editing the contact based on First Name
        :return:
        """
        f_name = input("Enter the First name whose contact you want to  edit")
        if f_name in self.list_of_contact:
            last_name = input("Enter the Last Name")
            city = input("Enter the City=")
            state = input("Enter the State=")
            zip = input("Enter the zip code=")
            phone_number = input("Enter the Phone Number=")
            email = input("Enter the Email Address=")
            detail_obj = {"first_name": f_name, "last_name": last_name, "city": city, "state": state,
                          "zip": zip, "phone_number": phone_number, "email": email}
            person = Contact(detail_obj)
            self.list_of_contact.pop(f_name)
            self.list_of_contact.update({f_name: person})
        else:
            print("Wrong Name or Conact Not Exist")
            self.logger.error("Wrong Name or Contact Not Exist")

    def menu(self, inp):
        """

        :param inp: choice
        :return:function
        """
        choice = {1: self.add_person, 2: self.display_all_contact, 3: self.delete_contact,
                  4: self.edit_contact, 5: self.search_by_city, 6: self.search_by_state, 7: self.sort_contact}
        return choice.get(inp)()

    def operation(self):
        """
        Print The menu
        :param address_book_name:AddressBook Name is given
        :return:
        """
        print("===============================")
        try:
            choice = {}
            inp = 0
            while (choice != 8):
                print("Welcome to Address Book Program")
                print("1)Add person")
                print("2)Show Address Book")
                print("3)Delete Contact")
                print("4)Edit Contact")
                print("5)Search By City")
                print("6)Search By State")
                print("7)Sorted Contact List")
                print("8)Exit")
                inp = int(input("Enter your choice"))
                self.menu(inp)
        except Exception as e:
            print(e)
            logger.error("Error is this ={} ".format(e))

    def search_by_city(self):
        """

        :return:print list of person live in specified City
        """
        print("Enter the City name")
        city = input()
        print("People Live in city {}".format(city))
        for i in self.list_of_contact.values():
            if city == i.get_city():
                print(i.get_name())

    def search_by_state(self):
        """

        :return: print list of person live in specified state
        """
        state = input("Enter The State Name")
        print("People Live in State {}".format(state))
        for i in self.list_of_contact.values():
            if state == i.get_state():
                print(i.get_name())

    def sort_contact(self):
        """

        :return: sorted lis of contacts
        """
        print("Sorted Contact List is ")
        for i in self.list_of_contact.values():
            print(sorted(i.get_all_details()))
