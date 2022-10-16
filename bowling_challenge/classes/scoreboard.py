from player import Player

class Game(Player):
    def __init__(self, game_name):
        self.game_name = game_name
        self.players=self.add_player()
    
    def add_player(self):
        players=[]
        num_of_players=input("Enter the number of players")
        for x in range(1, int(num_of_players)+1):
            player_name=input("Enter the player name")
            player_name=Player(player_name, 0)
            players.append(player_name)
        return players

    def play_full_game(self):
            for x in range(1, 11):
                for y in self.players:
                    y.current_roll=x
                    first_roll=int(input("Enter the first roll"))
                    if first_roll==10:
                        y.storage_of_rolls[x]=[10]
                    else:
                        second_roll=int(input("Enter the second roll"))
                        y.storage_of_rolls[x]=[first_roll, second_roll]
                    
                        y.storage_of_scores=y.return_score_board(y.return_score_per_frame())
                        print(y.storage_of_rolls)
                        print(f"{x} inning:\n----------\nYour roll's are:{y.storage_of_rolls[x]}\
                        \nYour current score is: {y.storage_of_scores[x]}\n\
                        Your total inning looks like\n\
                        {y.storage_of_scores}")









test=Game("Test")
test.play_full_game()
# test.play_full_game()

