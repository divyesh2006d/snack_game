from turtle import Turtle
from random import *

colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(choice(colors))
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.coordinate()


    def coordinate(self):
        x = randint(-260, 260)
        y = randint(-260, 260)
        self.goto(x, y)


    def refresh(self):
        self.clear()
        self.coordinate()