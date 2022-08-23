# # from calendar import isleap
# #First Challenge
# #Days in a month
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year) and month == 2:
#       return 29
#   return month_days[month-1]
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


#Calculator
#Add
from ast import Not
from art10 import logo

print(logo)

def add(n1,n2):
   return n1 + n2

#Substract
def substract(n1,n2):
   return n1 - n2

#Multiplication
def multiply(n1,n2):
   return n1 * n2

#Division
def divide(n1,n2):
   return n1 / n2


operations ={"+" : add,
             "-" : substract,
             "*" : multiply,
             "/" : divide}


def calulator():          
        num1 = int(input("What's the first number? \n"))
        for symbol in operations:
          print(symbol) 
        close = False
        while not close:  
              operation_symbol = input("Pick an operation from the above line: ")
              num2 = int(input("What's the next number? \n"))
              calculated_function = operations[operation_symbol]
              first_answer = calculated_function(num1 ,num2)
              print(f"{num1} {operation_symbol} {num2} = {first_answer}")
              
              a = input(f"Type 'y' to continue calculating with {first_answer} ,or type 'n' to exit.")
              if a =='y':
                    #  operation_symbol = input("Pick another operation : ")
                    #  num3 = int(input("What's the Third number? \n"))
                    #  calculated_function = operations[operation_symbol]
                    #  second_answer = calculated_function(first_answer ,num3)
                    #  print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
                    num1 = first_answer
                     
              elif a =='n':
                  close =True
                  calulator()
calulator()
                     
          