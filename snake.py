import turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        turtle1 = turtle.Turtle()
        turtle1.color("white")
        turtle1.shape("square")
        turtle1.penup()
        turtle1.setposition(0, 0)
        self.segments.append(turtle1)

        turtle2 = turtle.Turtle()
        turtle2.color("white")
        turtle2.shape("square")
        turtle2.penup()
        turtle2.setposition(-20, 0)
        self.segments.append(turtle2)

        turtle3 = turtle.Turtle()
        turtle3.color("white")
        turtle3.shape("square")
        turtle3.penup()
        turtle3.setposition(-40, 0)
        self.segments.append(turtle3)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)

    def add_segment(self):
        new_turtle = turtle.Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.setposition(self.segments[-1].position())
        self.segments.append(new_turtle)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()


    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)