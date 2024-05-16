# TODO-1 create page
from turtle import  Screen
from shemistan import Shemistan
from level import Level
from cars import Cars
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)
shen = Shemistan()
lvl = Level()
cars = Cars()


game_is_on = True
while game_is_on:
    time.sleep(lvl.cars_speed)
    screen.update()
    shen.move()
    # TODO-3 detect collision of top
    if shen.ycor() > 280:
        lvl.level_up()
        shen.new_lvl()

    for car in cars.segments:
        if shen.distance(car) < 40:
            game_is_on = False
            lvl.game_over()
    cars.create_car()
    cars.move_cars()
screen.exitonclick()
