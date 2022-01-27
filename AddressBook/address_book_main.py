import logging

from AddressBook.contact import Contact

logging.basicConfig(filename="address_book_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class AddressBookMain:

    def __init__(self):

        self.list_of_contact = dict()

    def add_person(self):
        """
        :return:updated list of contact
        """
        try:

            first_name = input("Enter the First name=")
            last_name = input("Enter the Last name=")
            city = input("Enter the City=")
            state = input("Enter the State=")
            zip = input("Enter the zip code=")
            phone_number = input("Enter the Phone Number=")
            email = input("Enter the Email Address=")
            person = Contact(first_name, last_name, city, state, zip, phone_number, email)
            self.list_of_contact.update({first_name: person.get_all_detail()})
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
            for k, y in self.list_of_contact.items():
                print(y)
        else:
            print("Address book is Empty")

    def delete_contact(self, f_name):
        """

        :param f_name: First Name of Contact person
        :return:True if Delete Successfull and False if Unsuccessfull
        """
        try:

            # f_name = input("Enter the First Name of whose Contact you wan to delete")
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
        f_name = input("Enter the First name whose conact you want to  edit")
        if f_name in self.list_of_contact:
            last_name = input("Enter the Last Name")
            city = input("Enter the City=")
            state = input("Enter the State=")
            zip = input("Enter the zip code=")
            phone_number = input("Enter the Phone Number=")
            email = input("Enter the Email Address=")
            person = Contact(f_name, last_name, city, state, zip, phone_number, email)
            self.list_of_contact.pop(f_name)
            self.list_of_contact.update({f_name: person.get_all_detail()})
        else:
            print("Wrong Name or Conact Not Exist")
            self.logger.error("Wrong Name or Contact Not Exist")

    def menu(self, inp):
        """

        :param inp: choice
        :return:function
        """
        choice = {1: self.add_person, 2: self.display_all_contact, 3: self.delete_contact,
                  4: self.edit_contact}
        return choice.get(inp)()

    def operation(self):
        print("===============================")
        try:
            choice = {}
            inp = 0
            address = AddressBookMain()
            print("Welcome to Address Book Program")
            print("1)Add person")
            print("2)Show Address Book")
            print("3)Delete Contact")
            print("4)Edit Contact")
            inp = int(input("Enter your choice"))


            address.menu(inp)
        except Exception as e:
            print(e)
            address.logger.error("Error is this ={} ".format(e))


