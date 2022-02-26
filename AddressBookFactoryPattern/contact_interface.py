from abc import abstractmethod


class contact:
    @abstractmethod
    def get_all_details(self):
        pass

    @abstractmethod
    def get_city(self):
        pass

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
