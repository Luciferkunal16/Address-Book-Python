from abc import abstractmethod


class AddressBookInterface:
    @abstractmethod
    def add_person(self):
        pass

    @abstractmethod
    def deisplay_all_contact(self):
        pass

    @abstractmethod
    def delete_contact(self):
        pass

    @abstractmethod
    def edit_contact(self):
        pass

    @abstractmethod
    def operation(self, address_book_name):
        pass

    @abstractmethod
    def search_by_city(self):
        pass

    @abstractmethod
    def search_by_state(self):
        pass

    @abstractmethod
    def sort_contact(self):
        pass

    @abstractmethod
    def display_list_of_addressbook(self):
        pass
