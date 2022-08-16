fruits = ["Strawberries","Nectarines","Apples","Graphes","Peaches","Cherries","Pears"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)

# First Challenge
#Average Height Exercise
student_heights = input("Input a list of student heights ").split()
for n in range(0,len(student_heights)):
   student_heights[n] = int(student_heights[n])
print(student_heights)
total = 0
i =0
for height in student_heights:
    i +=1
    total +=height
average = total / i
print(f"Average height of students is {round(average)} ")

#Second Challenge
#High Score Exercise
student_scores = input("Input a list of student scores ").split()
for n in range(0,len(student_scores)):
   student_scores[n] = int(student_scores[n])
print(student_scores)
x=0
for score in student_scores:
    if x < score:
        x = score
print(f"The highest score in the class is : {x}")

# for loop and range
total =0
for  number in range (1, 101):
    total += number
print(total)

#Third Challenge
#Adding Even Exercise
total =0
for  number in range (0, 101,2):
    total += number
print(total)
   
#Fourth Challenge
#Fizz Buzz Exercise
for number in range(1,101):
       if number % 3 == 0 and number % 5 == 0 :
           print("FizzBuzz")
       elif number % 5 == 0 :
           print("Buzz")
       elif number % 3 == 0 :
           print("Fizz")
       else:
           print(number)

##Final Project 
##PyPassword Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Pypassword Generator. ")
input_letters = int(input("How many letters would you like in your password? \n"))
input_symbols = int(input("How many symbols would you like? \n"))
input_numbers = int(input("How many numbers would you like? \n"))


#Easy level
password = ""
for char in range(1,input_letters +1):
    random_char = random.choice(letters)
    # print(random_char)
    password += random_char
for char in range(1,input_symbols +1):
    random_char = random.choice(symbols)
    # print(random_char)
    password += random_char
for char in range(1,input_numbers +1):
    random_char = random.choice(numbers)
    # print(random_char)  
    password += random_char
print(f"Here is your password: {password}")

#Hard level
password = []
newpass=""
for char in range(1,input_letters+1):
    let = random.choice(letters)
    password.append(let)
    
for char in range(1,input_symbols+1):
    sym = random.choice(symbols)
    password.append(sym)
    
for char in range(1,input_numbers+1):
    num = random.choice(numbers)
    password.append(num)
# print(password)
random.shuffle(password)
# print(password)

for char in password:
    newpass += char
print(f"Your new password is : {newpass}") 