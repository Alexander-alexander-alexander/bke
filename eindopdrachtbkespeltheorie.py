#Dit is de eindopdracht voor Speltheorie met Python (I2)
import random
from bke import EvaluationAgent, start, can_win, is_winner, validate, plot_validation


class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)
    
class MijnSpeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[4] == my_symbol:
            getal = getal + 50
        if board[2] == my_symbol:
            getal = getal + 45
        if board[0] == my_symbol:
            getal = getal + 30
        if board[6] == my_symbol:
            getal = getal + 40
#       Waarom werkt dit niet? kunt u dat uitleggen?
#       if can_win(board, my_symbol):
#           getal = getal + 10
        if can_win(board, opponent_symbol):
            getal = getal - 1000
        return getal



mijn_speler = MijnSpeler()
my_random_agent = MyRandomAgent()
validation_agent = my_random_agent

validation_result = validate(agent_x=mijn_speler, agent_o=validation_agent, iterations=5)

print (validation_result)
plot_validation(validation_result)

start(player_x=mijn_speler, player_o =my_random_agent)


