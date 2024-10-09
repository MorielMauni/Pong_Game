# Imports
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from score import Score
import time

# Screen 'Settings'
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # The screen will be updated with the 'update'

# Left and Right Paddles location
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

# Listner for the arrow keys
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# While loop for the game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # Makes the ball slower
    screen.update() # Refresh the screen from the 'tracer'
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with Right paddles(X, Y)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
    # Detect when paddle miss
    if ball.xcor() > 380: # Right side
        ball.reset_position()
        score.l_points()
    if ball.xcor() < -380: # Left side
        ball.reset_position()
        score.r_points()


screen.exitonclick()