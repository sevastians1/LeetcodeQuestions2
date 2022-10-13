from Classes.school import School
school= School('Ridgemont High') 
def sign_in():
    for z in range(0,3):
        user_sign_in=input("Who is signing in>>>")
        for x in school.staff:
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

def interface(person_at_terminal):
    print(person_at_terminal)
    access_level="Principal"
    selection=input(f"{school.name} Student Interface\n"+
    "----------\n"+
    f"Welcome, {vars(person_at_terminal)['name']} Your access level is {access_level}\n"+
    "What would you like to do?\n"+
    "Options:\n"
    "   1 List All Students\n"
    "   2 View Individual Student <student_id>\n"
    "   3 Add a Student\n"
    "   4 Remove a Student <student_id>\n"
    "   5 Quit\n")
    return selection


def options(selection):
    try:
        selection=int(selection)
        if selection==1:
            for x in school.students:
                print(vars(x)['name'])
        elif selection ==2:
            found_student=False
            student_id=input("Please enter student ID>>>")
            for x in school.students:
                if student_id==vars(x)['school_id']:
                    temp=vars(x)
                    print(f"{temp['name']} is a {temp['age']} year old {temp['role']} with a password of {temp['password']}. Student ID:{temp['school_id']}")
                    found_student=True
                    break
        
            if found_student==False:
                print("student ID not found")
        elif selection ==3:
            return
        elif selection ==4:
            # student_id=input("Please enter student ID>>>")
            return
        elif selection ==5:
            return
        elif selection>5:
            print("Invalid option please enter another option")
        selection=input("Please enter an option>>>")
        options(selection)
    except:
        selection=input("Please enter an option>>>")
        options(selection)
# person_at_terminal=sign_in()
person_at_terminal=school.staff[0]

print(vars(person_at_terminal)['name'])
selection=interface(person_at_terminal)
options(selection)