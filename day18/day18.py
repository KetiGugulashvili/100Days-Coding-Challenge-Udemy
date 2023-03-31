from turtle import Turtle, Screen
 # Challenge 1
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
for i in range(3, 11):
    for figure in range(i):
        timmy.forward(100)
        timmy.right(360/i)

screen = Screen()
screen.exitonclick()


