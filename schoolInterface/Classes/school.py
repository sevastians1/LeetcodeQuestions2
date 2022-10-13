from Classes.student import Student
from Classes.staff import Staff
class School:
    def __init__(self, name):
        self.name=name
        self.staff=Staff.load_all_staff()
        self.students=Student.load_all_students()
    ##takes username+password, returns user
    def sign_in(self):
        try:
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
        except:
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
    def list_students(self):
        for count, x in enumerate(self.students):
            print(count, x.name, x.school_id)
    def find_student_by_id(self, student_id):
        found_student=False
        for x in self.students:
            if student_id==x.school_id:
                temp=vars(x)
                print(f"{temp['name']} is a {temp['age']} year old {temp['role']} with a password of {temp['password']}. Student ID:{temp['school_id']}")
                found_student=True
                break
        if found_student==False:
                print("student ID not found")
    def create_a_student(self):
        temp_student={}
        student_info =input("Please enter student name>>>")
        temp_student['name']=student_info
        student_info =input("Please enter student age>>>")
        temp_student['age']=student_info
        student_info =input("Please enter student student_id>>>")
        temp_student['school_id']=student_info
        student_info =input("Please enter student role>>>")
        temp_student['role']=student_info
        student_info =input("Please enter student password>>>")
        temp_student['password']=student_info
        # print(temp_student)
        x=Student(**temp_student)
        # print(x)
        return x 
    def delete_a_student(self, student_to_delete_id):
        for count, x in enumerate(self.students):
            if x.school_id==student_to_delete_id:
                del self.students[count]        
    def print_options(self, selection, access_level):
        try:
            selection=int(selection)
            if selection==1:
                self.list_students()
            elif selection ==2:
                student_id=input("Please enter student ID>>>")
                self.find_student_by_id(student_id)
            elif selection ==3:
                x=self.create_a_student()
                self.students.append(x)
            elif selection ==4:
                student_to_delete_id=input("Please enter student ID to delete>>>")
                self.delete_a_student(student_to_delete_id)
            elif selection ==5:
                return
            else:
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

