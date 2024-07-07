from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.l_score, align="left", font=("Courier", 80, "normal"))
        self.goto(200, 200)
        self.write(self.r_score, align="right", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scorecard()

    def r_point(self):
        self.r_score += 1
        self.update_scorecard()
