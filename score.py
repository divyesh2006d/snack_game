from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f'score : {self.score}', align='center', font=('Courier', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('Game Over', align='center', font=('Courier', 24, 'normal'))

    def up(self):
        self.clear()
        self.score += 1
        self.update()