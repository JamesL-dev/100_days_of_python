# Imports
import turtle as turtle_module
import random

# Used to get the color list from the image file
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle_module.colormode(255)
kratos = turtle_module.Turtle()
kratos.speed("fastest")
kratos.penup()
kratos.hideturtle()

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

kratos.dot(20, random.choice(color_list))

kratos.setheading(225)
kratos.forward(250)
kratos.setheading(0)
number_of_dots = 100

for dot_count in range(0, number_of_dots):
    kratos.dot(20, random.choice(color_list))
    kratos.forward(50)
    if dot_count % 10 == 0:

        kratos.setheading(90)
        kratos.forward(50)
        kratos.setheading(180)
        kratos.forward(500)
kratos.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
