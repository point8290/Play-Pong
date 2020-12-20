import time
from turtle import Turtle,Screen

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Play Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
board = Turtle()
board.color("white")
board.penup()
board.pensize(5)
board.goto(0, 300)
board.setheading(270)
while board.ycor() > -350:
    board.pendown()
    board.forward(20)
    board.penup()
    board.forward(20)

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
left = 0
right = 0
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x(True)

    if ball.xcor() < -380 and ball.distance(left_paddle) > 50:
        scoreboard.rScore += 1
        scoreboard.update_score()
        ball.home()
        ball.bounce_x(False)

    if ball.xcor() > 380 and ball.distance(right_paddle) > 50:
        scoreboard.lScore += 1
        scoreboard.update_score()
        ball.home()
        ball.bounce_x(False)

screen.exitonclick()
