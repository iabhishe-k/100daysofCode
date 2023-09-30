from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 20)
        self.color("red")
        self.write(f"Game Over", align="center", font=("Arial", 32, "bold"))
        self.goto(0, 0)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))

    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_score()
