# from turtle import Turtle , Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# # timmy.speed(0)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)



from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

# from prettytable import PrettyTable
# table = PrettyTable(["Pokemon Name", "Type"])
# table.align["Pokemon Name"] = "l"  # Left align city names
# table.add_row(["Pikachu","Electric"])
# table.add_row(["Squirtle" , "Water"])
# table.add_row(["Charmandar", "Fire"])
# print(table)



# from prettytable import PrettyTable
# x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
# x.align["City name"] = "l"  # Left align city names
# x.padding_width = 1  # One space between column edges and contents (default)
# x.add_row(["Adelaide",1295, 1158259, 600.5])
# x.add_row(["Brisbane",5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])
# print(x)
#
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()