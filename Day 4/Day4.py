import random
random_integer = random.randint(0,4)
print(random_integer)

#Give outuput between 0 and 1
randomfloat = random.random() * 5
print(randomfloat)

#First Challenge 
#Head or Tail
if random_integer % 2 == 0:
    #head for even
    print(f"{random_integer} is head")
else :
    #tail for odd
    print(f"{random_integer} is tail")
    
#Offset and appending in lists
province_of_pakistan = ["Sindh","Punjab","Balochistan","KPK"]
province_of_pakistan.append("Gilgit")
province_of_pakistan.extend(["Kashmir"])
print(province_of_pakistan[random_integer])

#Second Challenge 
#Bank Roulette - Who will pay
#split string method
names_string = input("Give me everybody's names, seperated by a comma. \n")
names = names_string.split(",")
x = len(names)
random_integer = random.randint(0,x-1)
print(f"{names[random_integer]} is going to buy the meal today.")

#Index Errors and Nested list
fruits = ["Strawberries","Nectarines","Apples","Graphes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]
dirty_dozen = [fruits,vegetables]
print(dirty_dozen)


#Third Challenge 
#Treasure Map Exercise
row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]
map =[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])
selected_row= map[vertical-1]
selected_row[horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}")


#Final Project 
#Rock Paper Scissor

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
