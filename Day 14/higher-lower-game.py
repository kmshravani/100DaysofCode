from art import logo, vs
from game_data import data
import random
from replit import clear

#Format the account data into printable format
def format_data(account):
  '''Format the account data into printable format'''
  
  acc_name = account['name']
  acc_desc = account['description']
  acc_country = account['country']
  return f"{acc_name},a {acc_desc}, from {acc_country}"

##Use if statement to check if user is correct  
def check_answer(guess,a_followers, b_followers):
  '''Use if statement to check if user is correct '''
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


#Display art

score = 0
game_repeat = True
b = random.choice(data)

#Make game repeatable
while(game_repeat):

  #Generate a random accout from game data  
  # a = random.choice(data)
  # b = random.choice(data)
  # if a == b:
  #   b = random.choice(data)

  #Making account at position   B become next account at A 
  a = b 
  b = random.choice(data)
  while a == b:
    b = random.choice(data)

  print(f"Compare A: {format_data(a)}.")
  print(vs)
  print(f"Compare B: {format_data(b)}.")


  #Ask user to guess 
  guess = input("Who has more followers? Type 'A' or 'B : ").lower()

  #Check if user is correct
  ##Get follower count of each account 
  a_follower_count = a["follower_count"]
  b_follower_count =  b["follower_count"]

  ##Use if statement to check if user is correct 
  is_correct = check_answer(guess,a_follower_count, b_follower_count)

  #Clear the screen
  clear()
  print(logo)
  #Give some feedback to user based on guess 
  #Score keeping 
  if is_correct:
    score +=1
    print(f"You are right! Current score: {score}")
  else:
    game_repeat = False
    print(f"You are wrong. Final score: {score}")


