import random
class Scoreboard:
    def __init__(self, name):
        self.name = name
        # self.scoreboard=
    def roll(self):
        current_rolls=[]
        a=random.randint(0,10)
        current_rolls.append(a)
        if a==10:
            return current_rolls
        a=random.randint(0,10-a)
        current_rolls.append(a)
        return current_rolls
    def create_scoreboard(self):
        full_rollboard={}
        for x in range(1, 11):
            if x==10:
                a=self.roll()
                a=[10]
                if a[0]==10:#first roll in last frame is strike
                    for y in self.roll():
                        a.append(y)
                    if a[1]==10:
                        a.append(random.randint(0,10))
                elif a[0]+a[1]==10:#spare in last frame
                    a.append(random.randint(0,10))
                full_rollboard[x]=a
            else:
                full_rollboard[x]=self.roll()
        return full_rollboard
    def calculate_scoreboard(self, full_rollboard):
        # print(full_rollboard)
        full_rollboard[9]=[10]
        full_rollboard[8]=[10]
        print(full_rollboard)
        for x in range(1, 10):
            current_roll=full_rollboard[x]
            # print(current_roll)
            if len(current_roll)==1:#a strike
                if len(full_rollboard[x+1])>1:#if next roll is not strike, add two rolls
                    full_rollboard[x]=10+ full_rollboard[x+1][0]+full_rollboard[x+1][1]
                else: #if next roll is a strike, add next roll
                    full_rollboard[x]=10+full_rollboard[x+1][0]+full_rollboard[x+2][0]
            elif x==10:
                pass
            elif current_roll[0]+current_roll[1]==10:
                pass
        # print(full_rollboard)
        # for x in range(1, 10):
        #     current_roll=full_rollboard[x]
        #     if isinstance(current_roll, str):
        #         if current_roll=="strike":
        #             full_rollboard[x]=
        #         if current_roll=="spare":

        return full_rollboard

test=Scoreboard("test")
# testing=test.roll()
# print(testing)
# print(test.create_scoreboard())
print(test.calculate_scoreboard(test.create_scoreboard()))