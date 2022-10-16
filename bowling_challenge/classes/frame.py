import random


class Frame:
    def __init__(self, roll_number):
        self.roll_number=roll_number
        self.current_pins=self.make_current_roll()

    def random_bowl(self):
        current_rolls=[]
        a=random.randint(0,10)
        current_rolls.append(a)
        if a==10:
            return current_rolls
        a=random.randint(0,10-a)
        current_rolls.append(a)
        return current_rolls

    def make_current_roll(self):
        x=self.roll_number
        if x==10:
            a=self.random_bowl()
            # a=[10]
            if a[0]==10:#first roll in last frame is strike
                for y in self.random_bowl():
                    a.append(y)
                if a[1]==10:
                    a.append(random.randint(0,10))
            elif a[0]+a[1]==10:#spare in last frame
                a.append(random.randint(0,10))
            return a
        else:
            return self.random_bowl()


one=Frame(10)
# print(one.make_current_roll())
