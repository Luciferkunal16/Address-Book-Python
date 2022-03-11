from _pytest import monkeypatch

from AddressBook.address_book_main import AddressBookMain
from AddressBook.contact import Contact
from io import StringIO
from tud_test_base import set_keyboard_input, get_display_output


def test_contact_class_is_present():
    test_contact = Contact(contact_obj={"first_name": 'kunal', "last_name": 'batham', "city": 'city', "state": 'state',
                                        "zip": 'zip', "phone_number": '12121212', "email": 'kunal@gmail.com'})
    assert bool(test_contact) == True


def test_firstname_from_contact_class():
    test_contact = Contact(contact_obj={"first_name": 'kunal', "last_name": 'batham', "city": 'city', "state": 'state',
                                        "zip": 'zip', "phone_number": '12121212', "email": 'kunal@gmail.com'})
    assert test_contact.first_name == 'kunal'


def test_city_from_contact_class():
    test_contact = Contact(contact_obj={"first_name": 'kunal', "last_name": 'batham', "city": 'city', "state": 'state',
                                        "zip": 'zip', "phone_number": '12121212', "email": 'kunal@gmail.com'})
    assert test_contact.city == 'city'


def test_add_person():
    set_keyboard_input(['kunal', 'batham', 'noida', 'UP', '209', '9191919191', 'kuna@gmail.com'])
    test_address_book_obj = AddressBookMain("addressbook 1")
    test_address_book_obj.add_person()
    assert test_address_book_obj.list_of_contact is not None
