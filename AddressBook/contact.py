import logging


class Contact:
    def __init__(self, first_name, last_name, city, state, zip, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email
    def get_all_detail(self):
        return "First Name is {}".format(self.first_name),"Last name is {}".format(self.last_name),"Ciy is {}".format(self.city),"State is {} ".format(self.state),"Zip Code is {} ".format(self.zip),"Phone Number is {}".format(self.phone_number),"Email is {}".format(self.email)


