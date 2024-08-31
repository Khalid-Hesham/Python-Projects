import time

def speedTest_time(func):
  def wrapper():
    start = time.time()   
    char_cnt, word_cnt = func()
    end = time.time()
    speed1 = (word_cnt)/((end - start)/60) # WPM
    speed2 = (char_cnt/5)/((end - start)/60) # CPM/5 -> WPM
    avg_speed = (speed1 + speed2)/2
    print(f"Your Typing Speed Is: {avg_speed} Word per minute")
  return wrapper

@speedTest_time
def type_test():
  s1 = input("Type your name as fast as you can: ")
  char_count = len(s1)
  word_count = len(s1.split())
  return char_count, word_count

flag = True
while flag:
  type_test()
  flag = int(input("Enter 0 to exit\nEnter 1 to try again\n"))
