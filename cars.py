import turtle
from turtle import Turtle
from random import randint

# TODO-5 create cars with different colour on random y axis

turtle.colormode(255)


class Cars():
    def __init__(self):
        self.segments = []
        self.pos_x = 310
        self.create_car()
        self.move_cars()

    def random_color(self):
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)

        return (R, G, B)

    def create_car(self):
        pos_y = randint(-210, 210)
        new_segment = Turtle("square")
        new_segment.color(self.random_color())
        new_segment.shapesize(stretch_wid=1, stretch_len=2)
        new_segment.penup()
        new_segment.goto(self.pos_x, pos_y)
        self.segments.append(new_segment)

    # TODO-6 move car accross page right to left
    def move_cars(self):
        for cars in self.segments:
            new_x = cars.xcor() - 20
            cars.goto(new_x, cars.ycor())
