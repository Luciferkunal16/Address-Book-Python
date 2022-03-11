import logging
from AddressBook.address_book_main import AddressBookMain


class MulAddressBook:
    def __init__(self):
        self.book_dict = {}

    def display_list_of_addressbook(self):
        """
        used to display all existing address books
        :return: key value of Dictionary
        """
        for i in self.book_dict.keys():
            print(i)

    def create_new_addressbook(self):
        """
        Used for Create new addressbook
        :return:
        """
        address_book_name = input("Enter the AddressBook name")
        book_obj = AddressBookMain(address_book_name)
        book_obj.operation()
        self.book_dict[address_book_name] = book_obj

    def open_existing_addressbook(self):
        """
        For Open existing addressbook
        :return:
        """
        print("Number of AddressBook Available is {}".format(len(self.book_dict)))
        self.display_list_of_addressbook()
        address_book_name = input("Enter the AddressBook name which you want to edit")
        if address_book_name in self.book_dict.keys():
            print("Address Book Available in List")
            update_obj = self.book_dict.get(address_book_name)
            print(update_obj.operation())

        else:
            print("Address Book Empty or Name Mismatch")

    def operation(self):
        """
        used for creating and opening existing Book
        :return:
        """

        menu_opt = 0
        try:
            while menu_opt != 5:
                menu_opt = int(
                    input(
                        "1.Create New Address Book  2.Open Existing Address Book 3: Display All Address Book Name 4.Exit"))
                self.menu(menu_opt)
        except Exception as err:
            print(err)
            logging.ERROR("error occured-{}".format(err))

    def menu(self, choice=1):
        """
        Used for simulaing Menu
        :param choice:
        :return:
        """
        menu = {1: self.create_new_addressbook, 2: self.open_existing_addressbook, 3: self.display_list_of_addressbook,
                4: exit}
        return menu.get(choice)()


if __name__ == "__main__":
    try:
        obj = MulAddressBook()
        obj.operation()
    except Exception as e:
        logging.error(e)
        print(e)
