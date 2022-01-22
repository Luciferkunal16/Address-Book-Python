import logging

from AddressBook.contact import Contact

logging.basicConfig(filename='address_book_log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


class AddressBookMain:
    list_of_contact = list()

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
            self.list_of_contact.append(person.get_all_detail())
        except Exception as e:
            print(e)
            logging.info()
            logging.info()

    def display_all_contact(self):
        """

        :return:
        """
        print("Address Book is")
        for list in self.list_of_contact:
            for contact in list:
                print(contact)

    # def edit_contact(self):
    #     f_name = input("Enter the First Name ")
    #     for i in range(0,1):
    #         edit_person=Contact(i)
    #         print(edit_person)
    #
    #
    #
    #         print("All strings with given substring are : ")

    def menu(self, inp):
        """

        :param inp: choice
        :return:function
        """
        choice = {1: address.add_person, 2: address.display_all_contact, 3: exit}
        return choice.get(inp)()


if __name__ == "__main__":
    print("===============================")
    try:
        choice = {}
        inp = 0
        address = AddressBookMain()
        address.add_person()
        address.edit_contact()
        # while (inp != 3):
        #     print("Welcome to Address Book Program")
        #     print("1)Add person")
        #     print("2)Show Address Book")
        #     print("3)Exit")
        #     inp = int(input("Enter your choice"))
        #     address.menu(inp)
    except Exception as e:
        print(e)
        logging.INFO
        logging.error(e)
