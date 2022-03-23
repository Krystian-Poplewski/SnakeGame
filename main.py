from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
game_is_on = True


def quit_game():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(quit_game, "Escape")

scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        snake.grow()
        food.refresh()
        scoreboard.increase()
    if snake.is_wall_collision() or snake.is_tail_collision():
        scoreboard.reset()
        snake.reset()
    time.sleep(0.1)
