from turtle import Turtle
import random

FOOD_COLORS = ["red", "orange", "green", "blue", "yellow", "purple"]
FOOD_SHAPE = "circle"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a random location on the screen and change its color"""
        self.color(random.choice(FOOD_COLORS))
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
