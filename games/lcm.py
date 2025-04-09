import random as r
from engine import run_game
import math
def game_logic():
    a1 = (r.randint(1,100),r.randint(1,100),r.randint(1,100)) 
    question = " ".join(map(str, a1))
    answer = math.lcm(*a1)

    return question,answer

def play_lcm():
    description = "Find the smallest common multiple of given numbers."
    run_game(game_logic, description)
    
