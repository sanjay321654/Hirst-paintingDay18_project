import turtle
import random
import colorgram

turtle.colormode(255)
from turtle import Turtle, Screen

tom = Turtle()

color_list = [ (179, 63, 33), (24, 30, 64),
              (48, 35, 20), (240, 233, 78),
              (211, 144, 91), (143, 24, 38), (56, 28, 38), (117, 164, 215), (144, 24, 17), (54, 83, 141),
              (197, 78, 123), (62, 108, 61),
              (27, 47, 34), (29, 43, 121), (147, 64, 78), (92, 100, 195), (207, 90, 63), (144, 183, 166), (42, 80, 58),
              (189, 142, 156),
              (218, 125, 30), (91, 162, 68), (154, 222, 208), (149, 206, 225), (156, 187, 234), (245, 225, 5)]
tom.penup()
tom.speed("fastest")
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
no_of_dots = 100
tom.hideturtle()


for dots in range(1, no_of_dots + 1 ):

    tom.dot(20, random.choice(color_list))
    tom.forward(50)

    if dots % 10 == 0:

        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)



screen = Screen()
screen.exitonclick()
