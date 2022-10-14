# budget_object=[]
# import csv
# row=[7, 8, 9]
#     #classes/classes.pybudget_challenge/classes/classes.py
# with open("bowling_challenge/bowling_frame/bowling_instance.csv", "a", newline="") as f:
#     writer=csv.writer(f)
#     writer.writerow(row)
# with open("bowling_challenge/bowling_frame/bowling_instance.csv", "r") as f:
#     data=csv.DictReader(f, delimiter=",", skipinitialspace=True)
#     for x in data:
#         print(x)
class Bowling:
    def __init__(self):
        self.name = "Bowling"