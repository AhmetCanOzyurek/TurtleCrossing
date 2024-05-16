# TODO-2 create turtle in the mid-bottom and move forward only till top
from turtle import Turtle

POS_Y=  -260
class Shemistan(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.seth(90)
        self.teleport(0,POS_Y)

    def move(self):
        self.screen.listen()
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    def new_lvl(self):
        self.clear()
        self.goto(0,POS_Y)
