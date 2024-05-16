from turtle import Turtle


# TODO-4 Write level
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()
        self.cars_speed = 0.3
    def update_level(self):
        self.clear()
        self.goto(-200, 240)
        self.write(f"level : {self.level}", align="center", font=("Courier", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.update_level()
        # TODO-7 increase level and cars speed
        self.cars_speed *= 0.9

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))
