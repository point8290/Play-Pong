from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.lScore = 0
        self.rScore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lScore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rScore, align="center", font=("Courier", 80, "normal"))
