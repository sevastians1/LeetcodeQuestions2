from Classes.person import Person
import csv
class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id=school_id
    # with open(file, 'r') as f:
    #     data = csv.DictReader(f, delimiter=',', skipinitialspace=True)
    @staticmethod
    def load_all_students():
        list_of_students=[]
        file_location="/home/sevastians/Code/Assignments/week2/week2all-assignments/schoolInterface/Classes/data/students.csv"
        with open(file_location, "r") as f:
            data=csv.DictReader(f, delimiter=",", skipinitialspace=True)
            for x in data:
                # print(x)
                name=Student(**x)
                list_of_students.append(name)
        # print(list_of_students)
        return list_of_students

    @staticmethod  
    def create_a_student():
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

