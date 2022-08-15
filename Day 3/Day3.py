#if else statement
#Nested if and elif statements
print("Welcome to the rollercoaster.")
height = int(input("what is yout height in cm ? "))
bill = 0
if height >= 120:
    print("You can ride the rollcoaster!")
    age = int(input("What is your age? "))
    if age <12:
        bill = 5
        print("Please pay 5$")
    elif age>=12 & age <18:
        bill = 7
        print("Please pay 7$")
    else :
        bill = 12
        print("Please pay 12$")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" :
        #Add $3 to thier bill
        bill = bill + 3
    print(f"Your Fina bill is {bill}")
else:
    print("Sorry! you have to grow taller before you can ride.")

# one equal(=) means its assigning
# two equal(==) means its checking equality

#First Challenge
#Odd or even
number = int(input("Type any number.    "))
modulo = number % 2

if modulo == 0:
    print("Number is even.")
else:
    print("Number is odd.")
    
#Nested if and elif statements
# Second Challenge
#BMI Calculator

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in g : "))

BMI = weight /height*2

print(BMI)
if BMI < 18.5:
    print(f"Your BMI is {BMI} ,You are underweight")
elif BMI <= 25:
    print(f"Your BMI is {BMI} ,You are normal weight")
elif BMI <= 30:
    print(f"Your BMI is {BMI} ,You are overweight")
elif BMI <= 35:
    print(f"Your BMI is {BMI} ,You are obese")
elif BMI > 35:
    print(f"Your BMI is {BMI} ,You are underweight")

#Third Challenge
#Leap Year
#Every year has 365 days but leap year have 366 days one extra in february
#year/4 = evenly divisible,year/400 = evenly divisible ,for leap year
#year/100 = evenly divisible for normal year
year = int(input("Which year do youw want to check? "))
year1 = year % 4 == 0 & year % 100 != 0

if year % 4 == 0 :
    if year % 100 != 0 :
        print(f"{year} is leap year")
    else:
        if year % 400 == 0 :
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
else:
    print(f"{year} is not leap year")
    
Multiple if statements 

#Fourth Challenge
#Pizza Order
print("welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want ? S, M, or L ? ")
add_Pepperoni = input("Do you want pepperoni? Y or N ? ")
extra_cheese = input("Do you want extra cheese? Y or N ? ")
bill = 0
if size == "S" :
    bill = 15
    if add_Pepperoni =="Y" :
             bill = bill + 2
elif size == "M":
    bill = 20
    if add_Pepperoni =="Y" :
             bill = bill + 3
elif size == "L":
    bill = 25
    if add_Pepperoni =="Y" :
             bill = bill + 3

if extra_cheese == "Y" :
    bill = bill + 1
print(f"Your final bill is : {bill}")

Logical Operators

#Fifth Challenge
#Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower= name1.lower()
name2_lower= name2.lower()

t = name1_lower.count("t") + name2_lower.count("t")
r = name1_lower.count("r") + name2_lower.count("r")
u = name1_lower.count("u") + name2_lower.count("u")
e = name1_lower.count("e") + name2_lower.count("e")

first_digit =  t + r + u + e

l = name1_lower.count("l") + name2_lower.count("l")
o = name1_lower.count("o") + name2_lower.count("o")
v = name1_lower.count("v") + name2_lower.count("v")
e = name1_lower.count("e") + name2_lower.count("e")

second_digit =  l + o + v + e
total_str = str(first_digit)+str(second_digit)
total =int(total_str)
if total < 10 or total > 90:
    print(f"Your Score is {total} % ,You go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your Score is {total} % ,You are alright together .")
else:
    print(f"Your Score is {total} % ")

#Final Project
#Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''') 
print("Welcome to Treasue Island.")
print("Your Mission to find the treasure")
cross_road = input('You are at a cross road .Where do you wnat to go ? Type "left" or "right". \n' )
if cross_road =="left":
    lake = input("You come to a lake.There is an island in the middle of the lake.Type 'wait' to wait for a boat.Type 'swim' to swim across. \n")
    if lake == "wait" :
        colour=input("You arrive at the island unharmed.There is a house with 3 doors. One red , One yellow ,  and one blue. Which colour do you choose ? \n")
        if colour == "yellow" :
            print("You Win")
        else:
            print("Game Over")  
    else:
       print("Game Over")  
else:
    print("Game Over")   
