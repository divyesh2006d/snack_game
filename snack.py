from turtle import Turtle
from random import choice

start = [(0, 0), (-20, 0), (-40, 0)]
color = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta',
        'purple', 'brown', 'pink', 'orange', 'white']
move_distance = 20
up = 90
down = 270
left = 180
right = 0
class Snake:
    def __init__(self):
        self.l = []
        self.body()
        self.head = self.l[0]

    def body(self):
        for i in start:
            self.add_segment(i)


    def add_segment(self, i):
        n = Turtle('circle')
        n.color(choice(color))
        n.penup()
        n.goto(i)
        self.l.append(n)

    def reset(self):
        for i in self.l:
            i.goto(1000,1000)
        self.l.clear()
        self.body()
        self.head = self.l[0]

    def extend(self):
        self.add_segment(self.l[-1].position())

    def move(self):
        for n in range(len(self.l) - 1, 0, -1):  # fixed loop
            x = self.l[n - 1].xcor()
            y = self.l[n - 1].ycor()
            self.l[n].goto(x, y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
