from ast import Delete
from unicodedata import name


class Users:
    text=[['Fred', 'adsad'], ['Velma', 'sadasda']]
    def __init__(self, name, email_address, driver_licence):
        self.name=name
        self.email_address=email_address
        self.driver_licence=driver_licence
    def post(self):
        temp_text=input("Enter text here>>>>")
        print(self.name+"~~"+temp_text)
        Users.text.append([self.name, temp_text])
    @staticmethod
    def delete():
        try:    
            user=input("Which user is using")
            for count, i in enumerate(Users.text):
                if i[0]==user:
                    print(count, i)

            want_to_delete=input("Which one would you like to delete>>>")
            del Users.text[int(want_to_delete)]
        except: 
            print("User input does not match")





Fred=Users("Fred", "marley@gmail.com", "WDSA2131241")
# print(Fred.name, Fred.email_address, Fred.driver_licence)
Velma=Users("Velma", "velma@gmail.com", "SDADWA218321")
Fred.post()
print(Fred.text)
Fred.delete()
print(Fred.text)
