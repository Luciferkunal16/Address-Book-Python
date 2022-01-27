import self as self

from AddressBook.address_book_main import AddressBookMain


class MulAddressBook:
    def __init__(self):
        self.book_dict = {}

    def display_list_of_addressbook(self):
        for i in self.book_dict.keys():
            print(i)


if __name__ == "__main__":
    mul_obj = MulAddressBook()
    menu_opt = 0
    address_book = AddressBookMain()

    while menu_opt != 5:
        menu_opt = int(
            input("1.Create New Address Book  2.Open Existing Address Book 4: Diplay All Address Book Name 3.Exit"))
        if menu_opt == 1:
            address_book_name = input("Enter the AddressBook name")
            mul_obj.book_dict[address_book_name] = address_book.operation()
        elif menu_opt == 2:
            address_book_name = input("Enter the AddressBook name")
            if address_book_name in mul_obj.book_dict.keys():
                print("Address Book Available in List")
                mul_obj.book_dict.update({address_book_name: address_book.operation()})
            else:
                print("Address Book Empty or Name Mismatch")
        elif menu_opt == 4:
            mul_obj.display_list_of_addressbook()
