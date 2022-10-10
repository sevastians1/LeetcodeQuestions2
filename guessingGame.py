class Guessing_Game:
    answer=False
    def __init__(self, user_answer):
        self.user_answer=user_answer
    def guess(self, user_guess):
        if user_guess>self.user_answer:
            print("high")
        elif user_guess<self.user_answer:
            print("low")
        elif user_guess==self.user_answer:
            print("correct")
            self.answer=True
        else:
            self.answer=False
    def solved(self):
        print(self.answer)


game=Guessing_Game(10)
game.guess(11)
game.solved()
print(game.user_answer, game.answer)