import logging

from AddressBook.contact import Contact


class AddressBookMain:
    list_of_contact = dict()
    logging.basicConfig(filename="address_book_log.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def add_person(self,first_name,last_name,city,state,zip,phone_number,email):
        """

        :return:
        """
        try:
            # first_name = input("Enter the First name=")
            # last_name = input("Enter the Last name=")
            # city = input("Enter the City=")
            # state = input("Enter the State=")
            # zip = input("Enter the zip code=")
            # phone_number = input("Enter the Phone Number=")
            # email = input("Enter the Email Address=")
            person = Contact(first_name, last_name, city, state, zip, phone_number, email)
            self.list_of_contact.update({first_name:person.get_all_detail()})
        except Exception as e:
            print(e)
            self.logger.error("Error is {} ".format(e))
            self.logger.info()

    def display_all_contact(self):
        """

        :return:
        """
        if bool(self.list_of_contact):
            print("Address Book is")
            for k, y in self.list_of_contact.items():
                print(y)
        else:
            print("Address book is Empty")

    def delete_contact(self,f_name):
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
            self.logger.error("Wrong Name or Conact Not Exist")

    def menu(self, inp):
        """

        :param inp: choice
        :return:function
        """
        choice = {1: address.add_person, 2: address.display_all_contact, 3: address.delete_contact,
                  4: address.edit_contact, 5: exit}
        return choice.get(inp)()


if __name__ == "__main__":
    print("===============================")
    try:
        choice = {}
        inp = 0
        address = AddressBookMain()

        while inp != 5:
            print("Welcome to Address Book Program")
            print("1)Add person")
            print("2)Show Address Book")
            print("3)Delete Contact")
            print("4)Edit Contact")
            print("5)Exit")
            inp = int(input("Enter your choice"))
            address.menu(inp)
    except Exception as e:
        print(e)
        address.logger.error("Error is this ={} ".format(e))
