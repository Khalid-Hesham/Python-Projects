import random

def user_check(limit, u_number):
    low = 1
    high = limit
    c_guess = 0
    while c_guess != u_number:
        c_guess = random.randint(low, high)
        if c_guess < u_number:
            low = c_guess + 1
            print(f"Computer guess {c_guess} is too low")
        if c_guess > u_number:
            print(f"Computer guess {c_guess} is too high")
            high = c_guess - 1
    print(f"Yeah, Computer guess {c_guess} is correct.")


n = 1
while n != '0':    
  limit = int(input(f"Enter a limit for computer to search in: "))
  u_number = int(input(f"Enter your number between 1 and {limit}: "))
  user_check(limit, u_number)
  n = input("Press 1 to continue\nPress 0 to exit\n")