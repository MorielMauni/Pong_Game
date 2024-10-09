from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        '''
        Creats the Ball, white and circle
        '''
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        '''
        Make the ball move
        '''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        '''
        Bounce the ball when collistion Y
        '''
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        '''
        Bounce the ball when collistion X
        '''
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
