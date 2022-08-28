#Display art
import art14
from Gamedata import data
import random
import os

account_b = random.choice(data)
game_should_continue = True
count =0

while game_should_continue:
 print(art14.logo)
 def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return (f" {name} ,a {description} ,from {country}")
         
 #Generate random account from the game data
 account_a = account_b
 account_b = random.choice(data)
 
 while account_a == account_b:
     account_b = random.choice(data)
 
 print(f"Compare A : {format_data(account_a)}")
 print(art14.vs)
 print(f"Against B : {format_data(account_b)}")
 
 #ask the user for a guess 
 print(account_a["follower_count"])
 print(account_b["follower_count"])
 user_input = input("Who has more followers ? Type 'A' or 'B' : ").lower()
 os.system('cls')
 if user_input == "a" and account_a["follower_count"] > account_b["follower_count"]:
     count += 1
     print(f"You'r right .Current Score {count}")
    
 elif user_input == "b" and account_a["follower_count"] < account_b["follower_count"]:
     count += 1
     print(f"You'r right .Current Score {count}")
     
 else:
     game_should_continue = False
     print(f"Sorry , That's wrong .Final score : {count} ")
     
         
         

