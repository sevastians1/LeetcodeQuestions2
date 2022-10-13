from ast import Delete
from unicodedata import name


class Users:
    text=[['Fred', 'adsad'], ['Fred', 'post'], ['Velma', 'sadasda']]
    def __init__(self, name, email_address, driver_licence):
        self.name=name
        self.email_address=email_address
        self.driver_licence=driver_licence
        self.post_history=[]

    def post(self):
        temp_text=input("Enter text here>>>>")
        print(self.name+" says>>>"+temp_text)
        self.post_history.append(temp_text)
        Users.text.append([self.name, temp_text])


    def delete(self):
        try:    
            delete_num=0
            for count, posts in enumerate(self.post_history):
                print("Past Posts\n", count+1, posts)
                delete_num=count
            want_to_delete=int(input("Which one would you like to delete>>>"))-1
            for count, posts in enumerate(Users.text):
                # print(posts)
                if posts[1]==self.post_history[delete_num]:
                    del Users.text[count]
            del self.post_history[int(want_to_delete)]
        except: 
            print("User input does not match")


class PremiumUser(Users):
    def __init__(self, name, email_address, driver_licence):
        super().__init__(name, email_address, driver_licence)

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







