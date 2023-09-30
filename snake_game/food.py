from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(stretch_len=0.4, stretch_wid=0.4)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-26, 26)*10
        rand_y = random.randint(-26, 24)*10
        self.goto(rand_x, rand_y)
