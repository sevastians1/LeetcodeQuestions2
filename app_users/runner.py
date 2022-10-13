from freeuser import FreeUser
from premiumuser import PremiumUser


Fred=FreeUser("Fred", "marley@gmail.com", "WDSA2131241")
print(Fred.name, Fred.email_address, Fred.driver_licence)

Velma=PremiumUser("Velma", "velma@gmail.com", "SDADWA218321")
# Fred.post_history=['adsad', "post"]
Fred.post()
Fred.post()
# Fred.post()
Velma.post()
Velma.post()
Velma.post()

# Fred.delete()
# print(Users.text)
# print(Fred.post_history)
# # Fred.delete()
# print(Fred.text)
