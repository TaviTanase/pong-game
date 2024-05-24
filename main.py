from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.listen()

paddle1=Paddle((350,0))
paddle2=Paddle((-350,0))

ball=Ball()

scoreboard=Scoreboard()

screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.01)

    #colision&bounce
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce()

    if ball.distance(paddle1)<100 and ball.xcor()>330:
        ball.paddle_bounce()

    if ball.distance(paddle2)<100 and ball.xcor()<-330:
        ball.paddle_bounce()

    if ball.xcor()>380:
        ball.respawn()
        scoreboard.update2()

    if  ball.xcor()<-380:
        ball.respawn()
        scoreboard.update1()







screen.exitonclick()
