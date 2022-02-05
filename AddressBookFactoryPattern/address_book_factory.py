from AddressBookFactoryPattern.contact import Contact
from AddressBookFactoryPattern.address_book import AddressBook
from AddressBookFactoryPattern.multi_address_book import MultiAddressBook


class AddressBookFactory:

    def get_obj(self, name):
        """
        Get the objct of either single addresbook or multi addressbook
        :param name: String single or multi
        :return: obejct of desired type
        """
        if name == 'single':
            address_book_name = input("Enter the Address Book name")
            return AddressBook(address_book_name)
        elif name == "multi":
            return MultiAddressBook()


if __name__ == "__main__":
    factory = AddressBookFactory()
    print("1)Single AddressBook \n 2)Multi Addressbook  ")
    choice = int(input("Enter your choice"))
    if choice == 1:
        single_address_book = factory.get_obj("single")
        single_address_book.operation()
    elif choice == 2:
        multi_address_book = factory.get_obj("multi")
        multi_address_book.operation()
