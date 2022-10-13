from app_users import Users

class FreeUser(Users):
    def __init__(self, name, email_address, driver_licence):
        super().__init__(name, email_address, driver_licence)
    def post(self):
        # print(self.post_history, "You can post")
        # print(self.post_history)
        if len(self.post_history)>=2:
            print("Must be a premium user to post more then twice")
            return
        
        else:
            # print(self.post_history, "You can post", len(self.post_history))
            super().post()
            return
