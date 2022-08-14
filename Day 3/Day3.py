# #if else statement
# #Nested if and elif statements
# print("Welcome to the rollercoaster.")
# height = int(input("what is yout height in cm ? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollcoaster!")
#     age = int(input("What is your age? "))
#     if age <12:
#         bill = 5
#         print("Please pay 5$")
#     elif age>=12 & age <18:
#         bill = 7
#         print("Please pay 7$")
#     else :
#         bill = 12
#         print("Please pay 12$")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y" :
#         #Add $3 to thier bill
#         bill = bill + 3
#     print(f"Your Fina bill is {bill}")
# else:
#     print("Sorry! you have to grow taller before you can ride.")
#
# # one equal(=) means its assigning
# # two equal(==) means its checking equality

# #First Challenge
# #Odd or even
# number = int(input("Type any number.    "))
# modulo = number % 2

# if modulo == 0:
#     print("Number is even.")
# else:
#     print("Number is odd.")
    
# #Nested if and elif statements
# # Second Challenge
# #BMI Calculator

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in g : "))

# BMI = weight /height*2

# print(BMI)
# if BMI < 18.5:
#     print(f"Your BMI is {BMI} ,You are underweight")
# elif BMI <= 25:
#     print(f"Your BMI is {BMI} ,You are normal weight")
# elif BMI <= 30:
#     print(f"Your BMI is {BMI} ,You are overweight")
# elif BMI <= 35:
#     print(f"Your BMI is {BMI} ,You are obese")
# elif BMI > 35:
#     print(f"Your BMI is {BMI} ,You are underweight")

# #Third Challenge
# #Leap Year
# #Every year has 365 days but leap year have 366 days one extra in february
# #year/4 = evenly divisible,year/400 = evenly divisible ,for leap year
# #year/100 = evenly divisible for normal year
# year = int(input("Which year do youw want to check? "))
# year1 = year % 4 == 0 & year % 100 != 0

# if year % 4 == 0 :
#     if year % 100 != 0 :
#         print(f"{year} is leap year")
#     else:
#         if year % 400 == 0 :
#             print(f"{year} is leap year")
#         else:
#             print(f"{year} is not leap year")
# else:
#     print(f"{year} is not leap year")
    
#Multiple if statements 

# #Fourth Challenge
# #Pizza Order
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
