from unicodedata import name


class Users:
    def __init__(self, name, email_address, driver_licence):
        self.name=name
        self.email_address=email_address
        self.driverlicence=driver_licence
Fred=Users("Fred Marley", "marley@gmail.com", "WDSA2131241")
print(Fred.name, Fred.email_address, Fred.driverlicence)