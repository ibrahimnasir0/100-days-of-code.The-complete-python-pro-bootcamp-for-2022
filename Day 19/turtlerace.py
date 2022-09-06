from operator import is_
from turtle import Turtle ,Screen, color
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title='Make a bet',prompt ='Which turtle will win the race.Enter the color: ')
colors =['red','orange','blue','green','purple','yellow']
screen.title("Welcome to the turtle Race!")
import random
all_turtle = []
i=-100
for turtle_index in range(0,6):
        a = Turtle(shape='turtle')
        a.color(colors[turtle_index])
        a.penup()
        a.goto(x = -230,y =i)
        i += 50
        all_turtle.append(a)
is_race = False

if user_bet:
        is_race = True       
while is_race :
            
    for turtle in all_turtle:
        if turtle.xcor()>220:
                is_race = False
                winner_color = turtle.pencolor()
                if winner_color == user_bet:
                     style = ('Arial', 30, 'italic')
                     turtle. write('You Won!', font=style, align='right')
                     turtle. hideturtle()
                     print(f"You Won.The Winner Turtle is : {winner_color}")
                else:
                     style = ('Arial', 30, 'italic')
                     turtle. write('You Lose!', font=style, align='right')
                     turtle. hideturtle()   
                     print(f"You Lose.The Winner Turtle is : {winner_color}")
                      
        random_direction = random.randint(0,10)
        turtle.forward(random_direction)

screen.exitonclick()