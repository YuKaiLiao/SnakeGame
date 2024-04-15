from turtle import Turtle


class Snake:
    def __init__(self):
        self.turtles = []

        starting_position = [(0, 0), (-20, 0), (-40, 0)]

        for position in starting_position:
            new_turtle_element = Turtle("square")
            new_turtle_element.color("white")
            new_turtle_element.penup()
            new_turtle_element.goto(position)
            self.turtles.append(new_turtle_element)

        self.head = self.turtles[0]

    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
