# #Function
# def greet():
#     a = input("what is your name.\n")
#     print(a)
# greet()

# #Function with Argument
# def greet_with_name(name):
#     print(f"welcome {name}.\n""How are you.\n""What are you ding nowadays")
# greet_with_name("ibrahim")

# #Function with Two Argument
# def greet_with_two(name,location):
#     print(f"welcome {name}.\n""How are you doing nowadays.\n"f"How is a weather in {location}.")
# greet_with_two("ibrahim","Islamabad") 

# #Function with Poitional Keyword Argument
# def greet_with_two(name,location):
#     print(f"welcome {name}.\n""How are you doing nowadays.\n"f"How is a weather in {location}.")
# greet_with_two(location = "Islamabad",name = "ibrahim") 

## Calculating paint required on any area
# #Write your code below this line 👇
# def paint_calc(height,width,cover):
#     no_of_cans =(height *width)/cover
#     ans = round(no_of_cans)
#     print(f"You'll need {ans} cans of paint.")


# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


##prime checker
# #Write your code below this line 👇

# def prime_checker(number):
#     is_prime = True
#     for i in range(2,number):
#       if number % i == 0:
#           is_prime = False
          
#     if is_prime :
#      print(f"Its a prime number.")
#     else:
#      print(f"Its not a prime number.")   
                  
# #Write your code above this line 👆  
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)



# #Caesar Cipher
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#     #e.g. start_text = "meet me at 3"
#     #end_text = "•••• •• •• 3"
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# #TODO-1: Import and print the logo from art.py when the program starts.
# from art import logo
# print(logo)

# #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#   #Try running the program and entering a shift number of 45.
#   #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#   #Hint: Think about how you can use the modulus (%).
#   shift = shift % 26

#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")








