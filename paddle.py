from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(position)
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)

    def up(self):
        newy = self.ycor() + 20
        if self.ycor()<260:
            self.goto(self.xcor(), newy)

    def down(self):
        newy = self.ycor() - 20
        if self.ycor()>-260:
            self.goto(self.xcor(), newy)