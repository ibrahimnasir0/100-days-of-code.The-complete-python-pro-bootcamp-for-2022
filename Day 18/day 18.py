import turtle as t
# from turtle import Turtle,Screen
import random


timmy = t.Turtle()
t.colormode(255)
timmy.shape("circle")
# timmy.color('red')

##Challenge no 1
## Draw Square
  
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

# import heroes
# print(heroes.gen())




##Challange No 2
##Draw dashed line

# for _ in range(10):
#    timmy.forward(4)
#    timmy.penup()
#    timmy.forward(4)
#    timmy.pendown()


##Challange No 3
##Draw Triangle,Square,Pentagon,Hexagon,Haptagon,Octagon,Nonagon and Decagon.

# colors = ["gainsboro","bisque","tomato","yellow","lime",'cyan','aquamarine']


# def draw_shape(no_of_sides):
#    angle = 360/no_of_sides
#    for _ in range(no_of_sides):
#       timmy.forward(100)
#       timmy.right(angle) 
      
      
# for shape_side_n in range(3,11):
#    timmy.color(random.choice(colors))
#    draw_shape(shape_side_n)
      
# #Triangle
# for _ in range(3):
#    timmy.forward(100)
#    timmy.right(360/3) 
   
# #Square
# for _ in range(4):
#    timmy.forward(100)
#    timmy.right(360/4) 

# #pentagon
# for _ in range(5):
#    timmy.forward(100)
#    timmy.right(360/5) 
   
# #hexagon
# for _ in range(6):
#    timmy.forward(100)
#    timmy.right(360/6)
   
# #Heptagon
# for _ in range(7):
#    timmy.forward(100)
#    timmy.right(360/7) 

# #Octagon
# for _ in range(8):
#    timmy.forward(100)
#    timmy.right(360/8) 
   
# #Nonagon
# for _ in range(9):
#    timmy.forward(100)
#    timmy.right(360/9) 
   
# #Decagon
# for _ in range(10):
#    timmy.forward(100)
#    timmy.right(360/10) 



##Challange No 4
##Draw a random walk.


# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
   
#     random_color = (r,g,b)
#     return random_color
 
 
# timmy.speed("fastest")

# timmy.pensize(18)

# direction = [0,90,180,270]
# for _ in range(100):
#    timmy.color(random_color())
#    timmy.forward(100)
#    timmy.setheading(random.choice(direction))
   
##Challange No 5
##Make a Spirograph

# def draw_spirograph(size_of_gap):
#  for _ in range(int(360/size_of_gap)):
#    timmy.color(random_color())
#    timmy.circle(100)
#    timmy.setheading(timmy.heading() + size_of_gap)
# draw_spirograph(5)


# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('pic.jpg' , 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(350)
timmy.setheading(0)
no_of_dots =101

for dot_count in range(1,no_of_dots):
   timmy.dot(20,random.choice(color_list))
   timmy.forward(50)
   
   if dot_count % 10 == 0:
     timmy.setheading(90)
     timmy.forward(50)
     timmy.setheading(180)
     timmy.forward(500)
     timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()