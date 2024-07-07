from turtle import Turtle
X_COORDINATES = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in X_COORDINATES:
            self.add_tail(position)

    def add_tail(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.turtles.append(tim)

    def reset(self):
        for seg in self.turtles:
            seg.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend(self):
        self.add_tail(self.turtles[-1].position())

    def move(self):
        for j in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[j - 1].xcor()
            new_y = self.turtles[j - 1].ycor()
            self.turtles[j].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
