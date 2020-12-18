#Dit is de eindopdracht van Machine learning met Python (I3) 
import random

from bke import MLAgent, is_winner, opponent, load, validate, RandomAgent, plot_validation, train, start
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
random.seed(1)

my_agent = MyAgent(alpha=0.2, epsilon=0.1)

train(my_agent, 9000)

my_agent.learning = False

validation_agent = RandomAgent()

validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=1000)

print ("Hieronder vindt u de resultaten van mijn 1000 spelletjes tegen een random agent:")
print (validation_result)
print ("Klik de grafiek weg als u tegen mij wilt spelen!")
plot_validation(validation_result)

while True:
   answer = input("\nWilt u spelen met mij (en hooguit gelijkspelen)? (Ja/Nee):\n")
   if answer.lower().startswith("j"):
        print ("Wat leuk, daar gaan we!")
        print("\n")
        start(player_x=my_agent)
   else:
        print ("Oh...oke, jammer.")
        exit()
      



