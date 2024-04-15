from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# turtles = []
#
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
#
# for position in starting_position:
#     new_turtle_element = Turtle("square")
#     new_turtle_element.color("white")
#     new_turtle_element.penup()
#     new_turtle_element.goto(position)
#     turtles.append(new_turtle_element)
one_snake = Snake()
one_food = Food()

screen.listen()
screen.onkey(one_snake.up, "Up")
screen.onkey(one_snake.down, "Down")
screen.onkey(one_snake.left, "Left")
screen.onkey(one_snake.right, "Right")

screen.update()

game_is_on = True
number = 0

while game_is_on:
    one_snake.move()
    # turtles[0].left(90)
    screen.update()
    time.sleep(0.1)

    if one_snake.head.distance(one_food) < 15:
        one_food.refresh()

screen.exitonclick()
