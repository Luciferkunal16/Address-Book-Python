import logging

from AddressBook.contact import Contact


class AddressBookMain:
    list_of_contact = dict()
    logging.basicConfig(filename="address_book_log.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def __init__(self):
        self = dict()

    def add_person(self):
        """

        :return:
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
            self.list_of_contact[first_name] = person.get_all_detail()
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
            for i in self.list_of_contact.values():
                print(i)
        else:
            print("Address book is Empty")

    def delete_contact(self):
        try:

            f_name = input("Enter the First Name of whose Contact you wan to delete")
            if f_name in self.list_of_contact.keys():
                self.list_of_contact.pop(f_name)
                print("Contact is Deleted!!!!!!!")
            else:
                print("Contact Not Exist")
        except Exception as err:
            logging.error(err)
            print(err)

    def menu(self, inp):
        """

        :param inp: choice
        :return:function
        """
        choice = {1: address.add_person, 2: address.display_all_contact, 3: address.delete_contact, 4: exit}
        return choice.get(inp)()


if __name__ == "__main__":
    print("===============================")
    try:
        choice = {}
        inp = 0
        address = AddressBookMain()

        while inp != 4:
            print("Welcome to Address Book Program")
            print("1)Add person")
            print("2)Show Address Book")
            print("3)Delete Contact")
            print("4)Exit")
            inp = int(input("Enter your choice"))
            address.menu(inp)
    except Exception as e:
        print(e)
        address.logger.error("Error is this ={} ".format(e))
