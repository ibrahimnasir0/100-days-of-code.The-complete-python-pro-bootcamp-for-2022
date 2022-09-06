from turtle import Turtle ,Screen
timmy = Turtle()
screen = Screen()

def move_forwad() :
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def counter_clockwise():
    timmy.left(10)

def clockwise():
    timmy.right(10)
#
def move_clear():
    timmy.reset()

screen.listen()
# screen.onkey(key="w", fun=move_forwad)
screen.onkey(move_forwad, "w")
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=move_clear)
screen.exitonclick()