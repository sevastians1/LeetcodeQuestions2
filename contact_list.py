from audioop import reverse

class ContactList:

    def __init__(self, name, list_of_objects):
        self.name = name
        self.list_of_objects = list_of_objects

        self.sorts()

    # print to screen
    def __str__(self):
        for each in self.list_of_objects:
            print(each)
        return self.name

    # add the contacte
    def add_contact(self):
        name = input("What is the name: ")
        phone_number =  input("What is the Phone Number")
        self.list_of_objects.append({'name': name, 'number': phone_number})
        self.sorts()

    # sort when created, when called, and when add
    def sorts(self):
        self.list_of_objects.sort(key=lambda each: each['name'])
        # https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
        # self.list_of_objects = sorted(self.list_of_objects, key=lambda each: each['name'])

    # remove contacte if it existes
    def remove_contact(self):
        removed_name = input("How do you want to remove\n")
        for count, i in enumerate(self.list_of_objects):
            if i['name'] == removed_name:
                del self.list_of_objects[count]
                return
        print("did not find name\n") # if no name was found let the user know
        return

    # find same names in difrent lists
    def find_shared_contacts(self, other_list):
        temp_list = []
        for x in self.list_of_objects: # list one
            for y in other_list.list_of_objects: # list two
                if x == y:
                    temp_list.append(x)
        return print(temp_list)



    # @name.setter  (# this well set name)
    # def name(self):
    #     self.name = 'bob'
    #     return


friends = [{'name':'Alice','number':'867-5309'},{'name':'Zeed', 'number':'444-5555'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'},{'name':'Zeed', 'number':'444-5555'}]



my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)
print(my_friends_list)
print(my_work_buddies)
my_friends_list.remove_contact()
print(my_friends_list)



friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]