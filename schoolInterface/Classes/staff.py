from Classes.person import Person
import csv
class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
         super().__init__(name, age, role, password)
         self.employee_id=employee_id
    @staticmethod
    def load_all_staff():
        list_of_staff=[]
        file_location="/home/sevastians/Code/Assignments/week2/week2all-assignments/schoolInterface/Classes/data/staff.csv"
        with open(file_location, "r") as f:
            data=csv.DictReader(f, delimiter=",", skipinitialspace=True)
            for x in data:
                # print(x)
                name=Staff(**x)
                list_of_staff.append(name)
        # print(list_of_students)
        return list_of_staff   