import turtle
import time

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN: int = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.initial_state()
        self.head = self.segments[0]

    def initial_state(self):
        for initial_position in INITIAL_POSITIONS:
            new_segment = turtle.Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.goto(initial_position)
            new_segment.color("white")
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(STEP)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)
