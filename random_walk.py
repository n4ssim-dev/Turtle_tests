# Génération d'un chemin aléatoire
import turtle as t
import random as ra
t.colormode(255)

def random_color():
    r = ra.randint(0,255)
    g = ra.randint(0,255)
    b = ra.randint(0,255)
    rgb = (r,g,b)
    return rgb

franklin = t.Turtle()

colors = ["aquamarine", "gold", "indigo", "lime", "magenta", "navy", "olive", "purple", "teal", "violet"]
random_move = [lambda:franklin.right(ra.randint(0,360)), lambda:franklin.left(ra.randint(0,360))]
random_turn = [lambda: franklin.backward(ra.randint(15,75)),lambda:franklin.forward(ra.randint(15,75))]

franklin.pensize(6)
franklin.speed(7)

for turn in range(100):
    ra.choice(random_move)()
    ra.choice(random_turn)()
    franklin.color(random_color())

screen = t.Screen()
screen.exitonclick()