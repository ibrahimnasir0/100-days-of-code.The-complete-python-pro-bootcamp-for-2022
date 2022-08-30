def ammount(cost):
    print("Please Insert Coins.")
    Total = int(input("Number Of Five Rupee Coin ? ")) * 5
    Total +=  int(input("Number Of Two Rupee Coin ? "))  * 2
    Total +=  int(input("Number Of One Rupee Coin ? "))  * 1
    
    Refund_Ammount = Total - cost
    
    if Refund_Ammount < 0 :
        print(f"{Total} is not enough for this cofee")
        
    else: 
        Refund_Ammount = Total - cost
        resources["Money"] = cost + resources["Money"]
        print(f"Your Refund Amount is : {Refund_Ammount} Rupees")
        print("Your Cofee is ready.Hoping You like it. ")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 45,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 60,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 75,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money" : 0,
}



# def order_requirement(order):
#     for item in order:
#         if order[item] >= resources[item]:
#             print(f"sorry thier is no enough {item}")
#             is_game = False
#         else :
#             resources[item] = resources[item]-order[item]
            


    
is_game = True
while is_game:
     user_input = input("What would you like? (espresso/latte/cappuccino): ")
     if user_input =="report":
         print(f"Water : {resources['water']}ml")
         print(f"milk : {resources['milk']}ml")
         print(f"coffee : {resources['coffee']}g")
         print(f"Money : {resources['Money']}rs")
         
     elif  user_input == "espresso":
         
         resources["water"]=resources["water"] - MENU["espresso"]["ingredients"]["water"]
         resources["coffee"]=resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
         if resources["water"] < 0 or resources["coffee"] < 0 :
             print("Available Material is insufficient")
             resources["water"]=resources["water"] + MENU["espresso"]["ingredients"]["water"]
             resources["coffee"]=resources["coffee"] + MENU["espresso"]["ingredients"]["coffee"]
         else:
              print(f'You have to pay {MENU["espresso"]["cost"]} Rupees. ')
              ammount(MENU["espresso"]["cost"])
           
            #  drink = MENU['user_input']
            #  if order_requirement(drink["ingredients"]):
            #      print(f'You have to pay {MENU["espresso"]["cost"]} Rupees. ')
            #      ammount(MENU["espresso"]["cost"])
                 
                
         
         
     elif user_input =="latte":
         resources["water"]=resources["water"] - MENU["latte"]["ingredients"]["water"]
         resources["milk"]=resources["milk"] - MENU["latte"]["ingredients"]["milk"]
         resources["coffee"]=resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
         if resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0 :
             print("Available Material is insufficient")
             resources["water"]=resources["water"] + MENU["latte"]["ingredients"]["water"]
             resources["milk"]=resources["milk"] + MENU["latte"]["ingredients"]["milk"]
             resources["coffee"]=resources["coffee"] + MENU["latte"]["ingredients"]["coffee"]
         else:
              print(f'You have to pay {MENU["latte"]["cost"]} Rupees. ')
              ammount(MENU["latte"]["cost"])
              
     elif user_input =="cappuccino":
         resources["water"]=resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
         resources["milk"]=resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
         resources["coffee"]=resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
         if resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0  :
             print("Available Material is insufficient")
             resources["water"]=resources["water"] + MENU["cappuccino"]["ingredients"]["water"]
             resources["milk"]=resources["milk"] + MENU["cappuccino"]["ingredients"]["milk"]
             resources["coffee"]=resources["coffee"] + MENU["cappuccino"]["ingredients"]["coffee"]
         else:
              print(f'You have to pay {MENU["cappuccino"]["cost"]} Rupees. ')
              ammount(MENU["cappuccino"]["cost"])
     else :
         is_game = False