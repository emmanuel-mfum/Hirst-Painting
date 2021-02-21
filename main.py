#import colorgram
import random
import turtle
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     hue = (r, g, b)
#     rgb_colors.append(hue)
#
#
#
# print(rgb_colors)
turtle.colormode(255)
timmy = turtle.Turtle()

timmy.shape("turtle")
timmy.color("blue")
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setposition(-300.00, -250.00)
colors_list = [(218, 229, 220), (233, 220, 226), (218, 223, 230), (230, 207, 91), (225, 149, 91), (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145), (233, 81, 49), (202, 67, 27), (192, 186, 23), (174, 18, 13), (33, 129, 49), (7, 99, 37), (13, 64, 39), (12, 41, 76), (242, 203, 4), (139, 79, 92), (88, 13, 20), (53, 166, 76), (51, 23, 19), (180, 134, 146), (6, 64, 137), (213, 68, 75), (230, 170, 161), (49, 151, 191), (77, 133, 186), (175, 204, 176)]


def draw_dots():
    for n in range(10):
        timmy.dot(20, random.choice(colors_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


for x in range(10):
    draw_dots()
    timmy.penup()
    new_y = timmy.ycor() + 50
    timmy.setposition(-300.00, new_y)


screen = turtle.Screen()
screen.exitonclick()
