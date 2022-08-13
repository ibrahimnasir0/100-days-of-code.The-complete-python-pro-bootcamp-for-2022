#type conversion

from math import remainder


a = float(123)
print(type(a))

#Challenge
# Write a program that adds the digits in a 2 digit number 
# e.g. if the input was 35,then the output should be 3 +5 =8
  
n = input("Type a two digit number: ")
print(type(n))
first_digit = int(n[0])
second_digit = int(n[1])
two_digit_number = first_digit + second_digit
print(two_digit_number)

#Mathamatical Operations
print(3*3+3/3-3)
print(3*(3+3)/3-3)  #changing for answer 3

#Second Challenge
#Body Mass Index

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#"Your BMI is:",

bmi = int(weight) / (float(height)**2)
#f-string
print(f"Your BMI is: {int(bmi)}" )

#Third Challenge
#how many days weeks ,months we have left if we live until 90 years old by getting current age.
age = input ("What is your current age? ")

days = 365
weeks = 52
months = 12

totaldays = 60*365
totalweeks = 60*52
totalmonths = 60*12

userdays = int(age)*365
userweeks = int(age)*52
usermonths = int(age)*12

remainingdays = totaldays - userdays
remainingweeks = totalweeks - userweeks
remainingmonths = totalmonths - usermonths

print(f"you live {userdays} days, {userweeks} weeks and {usermonths} months in your life until now.")
print(f"You have {remainingdays} days , {remainingweeks} weeks and {remainingmonths} months left.")

#Todays Project
#TipCalculator   
print("Welcome to the tip calculator")
bill = float(input("what was the total bill ? "))
tip = input("What percentage tip would you like to give ?10, 12 or 15? ")
split = input("How many people to split the bill ? ")

totaltip = bill * (int(tip)/100)
totalbill = bill + totaltip
print(f"Each person should pay : {round(totalbill/int(split),2)}")