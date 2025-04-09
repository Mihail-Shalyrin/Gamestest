import random as r
from engine import run_game



def generate_progression():
    a=[]
    a.append(r.randint(1,5))
    g = r.randint(2,9)
    len1 = r.randint(5, 10)
    for i in range (1,len1):
       a.append(a[i-1]*g)
    index = r.randint(3,len1-1)
    anwser = a[index] 
    a[index] = ".."

    return " ".join(map(str, a)), anwser

    


def play_progression():
    """Запускает игру 'Геометрическая прогрессия'."""
    description = "What number is missing in the progression?"
    run_game(generate_progression, description)