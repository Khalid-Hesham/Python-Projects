import random

def computer_check(limit):
    c_random = random.randint(1, limit)
    u_guess = 0
    low = 1
    high = limit
    while c_random != u_guess:
        u_guess = int(input(f"Guess a number between {low} and {high}: "))
        if u_guess < c_random:
            low = u_guess + 1
            print(f"Your guess is too low")
        if u_guess > c_random:
            print(f"Your guess is too high")
            high = u_guess - 1
    print(f"Yeah, Your guess {u_guess} is correct.")


n = 1
while n != '0':    
  num = int(input(f"Computer limit is: "))
  computer_check(num)
  n = input("Press 1 to continue\nPress 0 to exit\n")