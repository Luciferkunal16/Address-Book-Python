from AddressBookFactoryPattern.contact_interface import contact


class Contact(contact):

    def __init__(self, contact_obj={}):
        self.first_name = contact_obj.get("first_name")
        self.last_name = contact_obj.get("last_name")
        self.city = contact_obj.get("city")
        self.state = contact_obj.get("state")
        self.zip = contact_obj.get("zip")
        self.phone_number = contact_obj.get("phone_number")
        self.email = contact_obj.get("email")

    def get_all_details(self):
        """

        :return: String of details
        """
        return "First Name is {}".format(self.first_name), "Last name is {}".format(self.last_name), "Ciy is {}".format(
            self.city), "State is {} ".format(self.state), "Zip Code is {} ".format(
            self.zip), "Phone Number is {}".format(self.phone_number), "Email is {}".format(self.email)

    def get_city(self):
        """

        :return: city of person
        """
        return self.city

    def get_state(self):
        """

        :return: State of person
        """
        return self.state

    def get_name(self):
        """

        :return: Full name of Person
        """
        return "NAME is {} {}".format(self.first_name, self.last_name)
