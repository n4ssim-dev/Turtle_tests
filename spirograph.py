import turtle
import random as ra
turtle.colormode(255)

t = turtle.Turtle()
t.speed("fastest")

def random_color():
    r = ra.randint(0,255)
    g = ra.randint(0,255)
    b = ra.randint(0,255)
    rgb = (r,g,b)
    return rgb

def draw_circle():
    t.circle(100)

for turn in range(72):
    draw_circle()
    t.right(5)
    t.color(random_color())

screen = turtle.Screen()
screen.exitonclick()