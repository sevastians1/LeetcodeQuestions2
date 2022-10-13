from Classes.student import Student
from Classes.staff import Staff
class School:
    def __init__(self, name):
        self.name=name
        self.staff=Staff.load_all_staff()
        self.students=Student.load_all_students()
        ##
    ##takes username+password, returns user
    def sign_in(self):
        for z in range(0,3):
            user_sign_in=input("Who is signing in>>>")
            for x in self.staff:
                if user_sign_in==vars(x)['name']:
                    for y in range (0, 3):
                        input_password=input("Enter password here>>>>")
                        if input_password==vars(x)['password']:
                            print("correct password")
                            return(x)
                        print("wrong password")
                    continue
            continue
        print("no users found here")
    
    def interface(self, person_at_terminal):
        # print(person_at_terminal)
        access_level=vars(person_at_terminal)['role']
        selection=input(f"{self.name} Student Interface\n"+
        "----------\n"+
        f"Welcome, {vars(person_at_terminal)['name']} Your access level is {access_level}\n"+
        "What would you like to do?\n"+
        "Options:\n"
        "   1 List All Students\n"
        "   2 View Individual Student <student_id>\n"
        "   3 Add a Student\n"
        "   4 Remove a Student <student_id>\n"
        "   5 Quit\n")
        return selection, access_level
    def print_options(self, selection, access_level):
        try:
            selection=int(selection)
            if selection==1:
                # print(self)
                for x in self.students:
                    print(x.name, x.school_id)
                    # print(vars(x))
            elif selection ==2:
                found_student=False
                student_id=input("Please enter student ID>>>")
                for x in self.students:
                    if student_id==x.school_id:
                        temp=vars(x)
                        print(f"{temp['name']} is a {temp['age']} year old {temp['role']} with a password of {temp['password']}. Student ID:{temp['school_id']}")
                        found_student=True
                        break
            
                if found_student==False:
                    print("student ID not found")
            elif selection ==3:
                x=Student.create_a_student()
                self.students.append(x)
                # for x in self.students:
                #     print(x.name)
                selection=input("Please enter a valid option>>>")
                self.print_options(selection, access_level)

            elif selection ==4:
                student_to_delete_id=input("Please enter student ID to delete>>>")
                for count, x in enumerate(self.students):
                    if x.school_id==student_to_delete_id:
                        del self.students[count]
                selection=input("Please enter a valid option>>>")
                self.print_options(selection, access_level)
            elif selection ==5:
                return
            elif selection>5:
                print("Invalid option please enter another option")
            selection=input("Please enter an option>>>")
            self.print_options(selection, access_level)
        except:
            selection=input("Please enter a valid option>>>")
            self.print_options(selection, access_level)
    # def __str__(self):
    #     for x in self.students:
    #         print(x.name, x.school_id)
    #         print("got here to self string")

