# Génération de formes ayant progressivement plus de côté (triangle > carré, etc ...)
from turtle import Turtle, Screen
import random as r

colors = ["aquamarine", "gold", "indigo", "lime", "magenta", "navy", "olive", "purple", "teal", "violet"]
f_loop = 360
n_turn = 3

franklin = Turtle()
franklin.shape("arrow")
franklin.color("black")

for turn in range(10):
    for turn_2 in range(n_turn):
        franklin.pensize(n_turn)
        franklin.speed(n_turn/2)
        franklin.forward(100)
        franklin.right(f_loop / n_turn)
    n_turn+=1
    franklin.color(r.choice(colors))

screen = Screen()
screen.exitonclick()