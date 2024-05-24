from turtle import Turtle
import random
x=random.randint(105,255)
y=random.randint(295,435)
random_heading=random.choice([x,y])
random_heading=random.choice([x,y])
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        self.setheading(random_heading)
    def move(self):
        #self.goto(x=self.xcor()+2,y=self.ycor()+2)
        self.forward(5)

    def bounce(self):
        self.setheading(360-self.heading())

    def paddle_bounce(self):
        self.setheading(540 - self.heading())

    def respawn(self):
        self.color("black")
        self.goto(0,0)
        random_heading2 = random.choice([x, y])
        random_heading2 = random.choice([x, y])
        self.setheading(random_heading2)
        self.color("white")