from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)

line = Turtle()
line.color("white")
line.hideturtle()
for i in range(32):
    if i < 15:
        line.setheading(90)
        line.forward(10)
        line.penup()
        line.forward(10)
        line.pendown()
    else:
        if i == 15:
            line.setheading(270)
            line.penup()
            line.goto(0, 0)
            line.forward(10)
            line.pendown()
            line.forward(10)
        else:
            line.setheading(270)
            line.penup()
            line.forward(10)
            line.pendown()
            line.forward(10)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detecting R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detecting L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
