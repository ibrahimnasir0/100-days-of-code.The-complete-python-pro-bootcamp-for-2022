# #First Challenge
# #Grading Program

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades ={}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if student_scores[key] >=90 :
#         student_grades[key]="Outstanding"
#     elif student_scores[key] >80 and student_scores[key] <90 :
#         student_grades[key]="Exceeds Expectation"    
#     elif student_scores[key] >=71 and student_scores[key] <=80 :
#         student_grades[key]="Acceptable"
#     elif student_scores[key] <=70 :
#         student_grades[key]="Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

# #Nesting Dictionaies
# travel_log = [
#       {"country": "France", "cities_visited":["paris","Lile","Dijon"]},
#       {"country": "Germany","cities_visited":["Berlin","hamburg","Stuttgart"],"Total_visit":10},
# ]
# print(travel_log)


# #Second Challenge
# #Adding Dictionary in a Dictionary using Function
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country,visited,cities):
#       new_country={}
#       new_country["country"]=country
#       new_country["visited"]=visited
#       new_country["cities"]=cities
#       travel_log.append(new_country)




# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# # Final Project
# # Secret Auction
# from operator import truediv
# import os
# from art9 import logo

# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     os.system('cls')
    
from art9 import logo
print(logo)

import os
bid ={}
answer =False
def highestbid(bidding_record):
    winner =""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount =bidding_record[bidder]
        if bid_amount > highest_bid:
          highest_bid = bid_amount
          winner = bidder
    print(f"The winner is {winner} and price is {highest_bid}.")
while not answer:
  name = input("What is your name. \n")
  amount =int(input("Enter your bid ammount. \n"))
  bid[name] = amount
  
  should_continue =input("Do you wanted to continue ?\n")
  if should_continue =="yes":
     os.system('cls')
  elif should_continue =="no":
      highestbid(bid)
      answer =True
      
    


    



