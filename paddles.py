from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, position):
        '''
        Shape, color, size and location(x, y) of the paddle
        '''
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        '''
        Makes the Paddle go up
        '''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        '''
        Makes the Paddle go down
        '''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)