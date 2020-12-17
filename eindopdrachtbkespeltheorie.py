import random
from bke import EvaluationAgent, start, can_win, is_winner


class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)
    
class MijnSpeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[4] == my_symbol:
            getal = getal + 5
        if can_win(board, my_symbol):
            getal = getal + 10
        if can_win(board, opponent_symbol):
            getal = getal - 1000
        return getal


mijn_speler = MijnSpeler()
my_random_agent = MyRandomAgent()

start(player_x=mijn_speler, player_o =my_random_agent)


