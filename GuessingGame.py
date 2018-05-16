import random


def guessing_game():
  whats_your_number = int(input("What's your number?"))
  number = int(random.randint(1,10))
  while whats_your_number != number:
    print("keep guessing")
    whats_your_number = int(input("What's your number?"))
    if whats_your_number == number: 
      print ("winner")
      break
guessing_game()
