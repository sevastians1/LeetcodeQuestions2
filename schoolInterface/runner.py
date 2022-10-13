from Classes.school import School
school= School('Ridgemont High') 

temp=school.interface(school.sign_in())
# print(temp)
school.print_options(*temp)