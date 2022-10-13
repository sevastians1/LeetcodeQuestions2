from app_users import Users


class PremiumUser(Users):
    def __init__(self, name, email_address, driver_licence):
        super().__init__(name, email_address, driver_licence)