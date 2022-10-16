from frame import Frame
import copy

class Player(Frame):
    def __init__(self, name, current_roll):
        self.name=name
        self.current_roll=current_roll
        self.storage_of_rolls=self.make_rollboard(current_roll)
        self.storage_of_scores=self.return_score_board(self.return_score_per_frame())


    def make_rollboard(self, how_many_rolls):
        current_rollboard={}
        for x in range(1, how_many_rolls+1):
            # print(x)
            current_frame=Frame(x)
            current_rollboard[x]=current_frame.current_pins
            
        return current_rollboard


    def return_score_per_frame(self):
        storage_of_scores=copy.copy(self.storage_of_rolls)
        for x in storage_of_scores:
            # print(x, storage_of_scores[x])
            if len(storage_of_scores[x])==1:#a strike
                if x==self.current_roll-1 and len(storage_of_scores[self.current_roll])==1:
                    ##if second to last roll is a strike and last roll is also a strike
                    storage_of_scores[x]="X"
                elif x==self.current_roll and self.current_roll!=10:
                    ##if last roll is a strike
                    storage_of_scores[x]="X"
                elif len(storage_of_scores[x+1])>1:
                    #if next roll is not strike, add two frames
                    storage_of_scores[x]=10+ storage_of_scores[x+1][0]+storage_of_scores[x+1][1]
                else: #if next roll is a strike, add next two rolls
                    storage_of_scores[x]=10+storage_of_scores[x+1][0]+storage_of_scores[x+2][0]
            
            elif x==10 and len(storage_of_scores[x])==3:
                #if in last frame
                storage_of_scores[x]=storage_of_scores[x][0]+storage_of_scores[x][1]+storage_of_scores[x][2]
            elif storage_of_scores[x][0]+storage_of_scores[x][1]==10:
                #if spare
                if x==self.current_roll:
                #if its the last frame and not 10
                    storage_of_scores[x]="/"
                else:
                    storage_of_scores[x]=10+storage_of_scores[x+1][0]
            else:
                storage_of_scores[x]=storage_of_scores[x][0]+storage_of_scores[x][1]
        return storage_of_scores


    def return_score_board(self, storage_of_scores):
        accumulating_score=0
        for x in storage_of_scores:
            if isinstance(storage_of_scores[x], str):
                return storage_of_scores
            accumulating_score+=storage_of_scores[x]
            storage_of_scores[x]=accumulating_score
        return storage_of_scores



Jim=Player("Jim", 0)
print(Jim.storage_of_scores)