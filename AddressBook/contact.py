import logging


class Contact:
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

    def set_last_name(self, l_name):
        """
        For setting the first name
        :return:
        """
        self.last_name = l_name

    def set_city(self, city):
        """
        For seting  the first name
        :return:
        """
        self.city = city

    def set_state(self, state):
        """
        For setting  the State
        :return:
        """
        self.state = state

    def set_zip_code(self, zip_code):
        """
        For setting  the zip code
        :return:
        """
        self.zip = zip_code

    def set_phone_number(self, phone_number):
        """
        For setting  the phone Number
        :return:
        """
        self.phone_number = phone_number

    def set_email(self, email):
        """
        For setting  the email
        :return:
        """
        self.email = email
