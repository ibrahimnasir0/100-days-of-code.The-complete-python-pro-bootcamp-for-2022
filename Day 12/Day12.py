import random
from art12 import logo
random_no = random.randint(1,100)
# print(random_no)
print(logo)
print("Welcome to the number guessing game")
print("I am thinking of number between 1 and 100")
user_choice = input('Choose Difficulty .Type "easy" or "hard" : ')
if user_choice =="easy":
    chances = 10
elif user_choice =="hard":
    chances = 5

is_game = False
while not is_game :
     print(f"You have {chances} attempts remaining to guess the number.")        
     user_guess = int(input("Make a guess : "))
     if chances == 1:
         is_game =True
         print("You've run out of guesses, you lose.")
     elif user_guess < random_no:
         print("Too Low")
         chances -= 1
     elif user_guess > random_no:
         print("Too High")
         chances -= 1
     elif user_guess == random_no:
         print(f"You got it .The answer was {user_guess}")
         is_game =True
     
         
         
         