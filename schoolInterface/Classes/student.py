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
                print(x)
                name=Student(**x)
                list_of_students.append(name)
        # print(list_of_students)
        return list_of_students
