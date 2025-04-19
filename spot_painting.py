# Création avec colorgram & python turtle d'un spot painting dans le style de l'artiste Damien Hirst

import colorgram as cg
import turtle
import random
turtle.colormode(255)

image_link = "./images/spot_painting.jpg"

def extract_colors(image):
    """Extract a list of 30 colors from an image and turns it into a rgb tuple, the argument is the image link."""
    color_list = cg.extract(image, 30)
    color_palette_list = []

    for color in color_list:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)

        color_palette_list.append(new_color)

    color_palette = tuple(color_palette_list)
    print(color_palette)

# Extracted colors from the image_link
colors_palette = ((204, 165, 107), (239, 246, 241), (237, 240, 245), (155, 73, 46), (174, 154, 37), (51, 93, 124), (224, 201, 133), (139, 31, 20), (132, 163, 185), (201, 90, 69), (46, 123, 86), (13, 100, 73), (70, 48, 39), (99, 72, 74), (147, 179, 146), (235, 175, 164), (163, 141, 158), (55, 46, 50), (184, 206, 171), (18, 85, 90), (147, 18, 22), (41, 61, 74), (80, 146, 128), (187, 83, 87), (41, 66, 88), (108, 126, 151), (15, 72, 69), (175, 192, 213))
# colors_palette = extracts_colors(image_link)
y_coord = -200

t = turtle.Turtle()
t.hideturtle()
t.pensize(10)
t.speed("fastest")
t.penup()
t.goto(-200,-200)
t.pendown()


def draw_circle(n_loop):
    global y_coord
    for loop in range(n_loop):
        t.pendown()
        t.color(random.choice(colors_palette))
        t.circle(5)
        t.penup()
        t.forward(50)
        if (loop + 1) % 10 == 0:
            y_coord += 50
            t.goto(-200, y_coord)

draw_circle(100)

screen = turtle.Screen()
screen.exitonclick()