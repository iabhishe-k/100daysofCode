from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def walls():
    turtle = Turtle()
    turtle.up()
    turtle.color("white")
    turtle.hideturtle()
    turtle.width(5)
    turtle.goto(-280, -280)
    turtle.down()
    turtle.fd(560)
    turtle.left(90)
    turtle.fd(540)
    turtle.left(90)
    turtle.fd(560)
    turtle.left(90)
    turtle.fd(540)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
walls()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

sleep_time = 0.1
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move_snake()

    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    if snake.head.xcor() > 275 or snake.head.xcor() < -275 or snake.head.ycor() > 255 or snake.head.ycor() < -275:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()

    if sleep_time > 0.02:
        sleep_time -= 0.00001


screen.exitonclick()
