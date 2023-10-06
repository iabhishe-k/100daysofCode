from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

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
        self.update_score()
