import logging

import self as self

from AddressBook.address_book_main import AddressBookMain

logging.basicConfig(filename="address_book_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
class MulAddressBook:
    def __init__(self):
        self.book_dict = {}

    def display_list_of_addressbook(self):
        """

        :return: key value of Dictionary
        """
        for i in self.book_dict.keys():
            print(i)




if __name__ == "__main__":
    mul_obj = MulAddressBook()
    menu_opt = 0

    try:

        while menu_opt != 5:
            menu_opt = int(
                input("1.Create New Address Book  2.Open Existing Address Book 3: Display All Address Book Name 4.Exit"))
            if menu_opt == 1:
                address_book_name = input("Enter the AddressBook name")
                book_obj = AddressBookMain(address_book_name)
                book_obj.operation(address_book_name)
                mul_obj.book_dict[address_book_name] = book_obj


            elif menu_opt == 2:
                print("Number of AddressBook Available is {}".format(len(mul_obj.book_dict)))
                mul_obj.display_list_of_addressbook()
                address_book_name = input("Enter the AddressBook name which you want to edit")
                if address_book_name in mul_obj.book_dict.keys():
                    print("Address Book Available in List")
                    update_obj = mul_obj.book_dict.get(address_book_name)
                    print(update_obj.operation(address_book_name))

                else:
                    print("Address Book Empty or Name Mismatch")
            elif menu_opt == 3:
                mul_obj.display_list_of_addressbook()
            elif mul_obj == 4:
                exit()
    except Exception as err:
        print(err)
        logging.ERROR("error occured-{}".format(err))

