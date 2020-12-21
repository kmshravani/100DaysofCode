from art import logo, vs

from game_data import data
import random

#Format the account data into printable format
def format_data(account):
  '''Format the account data into printable format'''
  
  acc_name = account['name']
  acc_desc = account['description']
  acc_country = account['country']
  return f"{acc_name},a {acc_desc}, from {acc_country}"
def check_answer(guess,a_followers, b_followers):
  

#Display art
print(logo)
#Generate a random accout from game data  
a = random.choice(data)
b = random.choice(data)
if a == b:
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


#Give some feedback to user based on guess 

#Scpre keeping 

#Make game repeatable 

#Making account at position   B become next account at A 

#Clear the screen
