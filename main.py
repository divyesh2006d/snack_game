from turtle import *
import snack
import food
import time
import score

t = Turtle()
s = Screen()
s.bgcolor("black")
s.title("my Snake game")
s.tracer(0)
s.listen()
s.setup(600,600)
t.penup()
fno = 0

snack = snack.Snake()
food = food.Food()
score = score.Score()

s.onkey(key='Up', fun=snack.up)
s.onkey(key='Down', fun=snack.down)
s.onkey(key='Left', fun=snack.left)
s.onkey(key='Right', fun=snack.right)

game = True
while game:
    s.update()
    time.sleep(0.3)
    snack.move()

    #collision with wall
    if snack.head.xcor() > 280 or snack.head.ycor() < -280 or snack.head.ycor() > 280 or snack.head.xcor() < -280:
        # game = False
        # score.game_over()
        score.reset_score()
        snack.reset()

    #collision with tail
    for j in snack.l:
        if j == snack.head:
            pass
        elif snack.head.distance(j) < 10:
            # game = False
            # score.game_over()
            score.reset_score()

    #collision with food
    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend()
        score.up()

s.exitonclick()