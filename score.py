from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt','r') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f'score : {self.score}  High Score : {self.high_score}', align='center', font=('Courier', 24, 'normal'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color('red')
    #     self.write('Game Over', align='center', font=('Courier', 24, 'normal'))

    def up(self):
        self.score += 1
        self.update()