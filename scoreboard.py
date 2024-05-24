from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points1 = 0
        self.points2 = 0
        self.goto(x=0,y=260)
        self.hideturtle()
        self.color("white")
        self.write(f"{self.points2}               {self.points1}",move=False,align="center",font=("Arial",30,"normal"))

    def update1(self):
        self.points1=self.points1+1
        self.clear()
        self.write(f"{self.points2}               {self.points1}",move=False,align="center",font=("Arial",30,"normal"))

    def update2(self):
        self.points2 = self.points2 + 1
        self.clear()
        self.write(f"{self.points2}               {self.points1}", move=False, align="center",font=("Arial", 25, "normal"))