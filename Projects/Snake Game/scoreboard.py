from turtle import Turtle, right

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
maximum = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.h_score = ''
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as file:
            content = file.read()
        self.write(f"Score: {self.score} High Score: {content}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.h_score = str(self.high_score)
            with open("data.txt", "w") as file:
                file.write(self.h_score)
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
        #self.goto(0, 0)
        #self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

