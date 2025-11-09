import turtle
import random


turtle.colormode(255)
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor(35, 58, 119)


divider_pen = turtle.Turtle()
divider_pen.color(255, 212, 31)
divider_pen.pensize(10)
divider_pen.penup()
divider_pen.goto(-500, 0)
divider_pen.pendown()
divider_pen.forward(1000)
divider_pen.hideturtle()


tooga = turtle.Turtle()
tooga.shape('turtle')
tooga.color(9, 185, 13)
tooga.pencolor(0, 128, 0)
tooga.turtlesize(3, 3, 3)
tooga.penup()


def draw_star(turtle_obj, size, color):
    turtle_obj.color(color)
    turtle_obj.pensize(2)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.right(144)
    turtle_obj.end_fill()
    turtle_obj.penup()


start_x   = -400
y_pos     = -100
step      = 200
num_stars = 5
size_star = 80
colors    = [
    (255, 215,   0),
    (255,   0,   0),
    (0,   255,   0),
    (0,   255, 255),
    (255,   0, 255)
]


for i in range(num_stars):
    tooga.goto(start_x + i * step, y_pos)
    draw_star(tooga, size_star, colors[i % len(colors)])

tooga.hideturtle()
screen.mainloop()