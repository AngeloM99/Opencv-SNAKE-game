from turtle import Turtle, Screen
from colour_randomisation import color_randomisation
import random

# Capitalise the constant
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.StartingPos = [(0, 0), (-20, 0), (-40, 0)]
        # You can call this function to run when the class has initiated.
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.StartingPos:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color(color_randomisation())
        new_segment.pd()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        # We will have to move the square from the last to the first.
        # For loop in reverse order

        for seg_num in range(len(self.segments) - 1, 0, -1):  # List counting from 0, hence len(segment)-1
            # Get a hold of the second to last segment position.
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Tell the last square to goto the second to last position
            self.segments[seg_num].goto(new_x, new_y)
        # Get hold of the first segment
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(0,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]