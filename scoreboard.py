from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"Left Player = {self.l_score}", align="center", font=("courier", 16, "normal"))
        self.goto(150, 250)
        self.write(f"Right Player = {self.r_score}", align="center", font=("courier", 16, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
