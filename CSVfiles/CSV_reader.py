class Pets:
    def __init__(self, name, age, breed):
        self.name=name
        self.age=age
        self.breed=breed
    def print_name(self):
        print(f"{self.name} is a very loving and eccentric {self.age} year old {self.breed}")
def animal_search(input):
    try:
        animal_file_location=f"./data/{input}.csv"
        f=open(animal_file_location, "r")
        lines=(f.read().split("\n"))
        del lines[0]
        names=[x.split(",")for x in lines]
        # print(names)
        for count, x in enumerate(lines):
            name=names[count][0]
            name=Pets(names[count][0], names[count][1], names[count][2])
            name.print_name()
        f.close()
    except:
        print(f"Sorry, we don't have any {input} here")

input=input("Enter animal here>>>")
animal_search(input)