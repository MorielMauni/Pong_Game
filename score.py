from turtle import Turtle, Screen

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        '''
        Makes the scoreboard
        '''
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_points(self):
        '''
        Adds points the the left side
        '''
        self.l_score += 1
        self.update_score()

    def r_points(self):
        '''
        Adds points the the right side
        '''
        self.r_score += 1
        self.update_score()