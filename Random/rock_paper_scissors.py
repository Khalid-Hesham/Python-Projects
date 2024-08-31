import random

def play():
    u_choose = input("Chooes 's' for scissors, 'p' for paper, 'r' for rock: ")
    c_choose = random.choice(['p','r','s'])
    
    if u_choose == c_choose:
        return "It's Draw"
    
    if is_win(u_choose, c_choose):
        return f"Computer choose {c_choose} and You won"

    return f"Computer choose {c_choose} and You lost"


def is_win(u_choose, c_choose):
    if((u_choose == 'r' and c_choose == 's') or (u_choose == 's' and c_choose == 'p') or (u_choose == 'p' and c_choose == 'r')):
        return True
    else:
        return False

n = 1
while n != '0':    
  print(play())
  n = input("Press 1 to continue\nPress 0 to exit\n")