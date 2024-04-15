from turtle import Turtle
from random import Random


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(1, 1)
        self.speed(0)
        random_obj = Random()
        self.goto(random_obj.randint(-280, 280), random_obj.randint(-280, 280))

    def refresh(self):
        random_obj = Random()
        self.goto(random_obj.randint(-280, 280), random_obj.randint(-280, 280))