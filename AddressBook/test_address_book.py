from AddressBook.address_book_main import AddressBookMain
from AddressBook.contact import Contact


def test_add_person_method():
    test_address = AddressBookMain()
    initial_list = test_address.list_of_contact.copy()
    test_address.add_person("kunal", "batham", "fgr", "UP", 209601, 9198559711, "gmail.com")
    final_list = test_address.list_of_contact
    assert initial_list != final_list


def test_init_function_contact_class():
    person = Contact("kunal", "batham", "fgr", "UP", 209601, 9198559711, "gmail.com")
    assert person.get_all_detail() != 0


def test_delete_contact():
    test_address_class = AddressBookMain()
    test_address_class.add_person("kunal", "batham", "fgr", "UP", 209601, 9198559711, "gmail.com")

    assert test_address_class.delete_contact("kunal") == True
