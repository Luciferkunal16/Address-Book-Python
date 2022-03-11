import logging

from AddressBook.contact import Contact

logging.basicConfig(filename="address_book_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class AddressBookMain:
    """
    Program for operations of AddressBook
    """

    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.list_of_contact = dict()

    def add_person(self):
        """
        use to add person to the list by inputing details of person details
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
            personObj = self.list_of_contact.get(f_name)
            print('Enter what you want to edit')
            print('1)Last Name')
            print('2)City')
            print('3)State')
            print('4)Zip code')
            print('5)Phone_number')
            print('6)Email_Address')
            choice = int(input('Enter the Choice in numeric'))
            update_value = input("enter the updated value")
            update_dict = {1: personObj.set_last_name, 2: personObj.set_city, 3: personObj.set_state,
                           4: personObj.set_zip_code, 5: personObj.set_phone_number, 6: personObj.set_email}
            update_dict.get(choice)(update_value)
            self.list_of_contact.update({f_name: personObj})
        else:
            print("Wrong Name or Contact Not Exist")
            self.logger.error("Wrong Name or Contact Not Exist")

    def menu(self, inp):
        """

        :param inp: choice
        :return:function
        """
        choice = {1: self.add_person, 2: self.display_all_contact, 3: self.delete_contact,
                  4: self.edit_contact, 5: self.search_by_city}
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

            print("Welcome to Address Book Program")
            print("1)Add person")
            print("2)Show Address Book")
            print("3)Delete Contact")
            print("4)Edit Contact")
            print("5)Search By City")

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
