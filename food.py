from turtle import Turtle , Screen
from snake import snake
import random
from scorebord import score_bord
import time


class food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.food()
        
# whare to put the food
        
    def food_location(self):
        self.pos_x = random.randint(-280,280)
        self.pos_y = random.randint(-280,280)
        self.setposition(self.pos_x,self.pos_y)

#charecteristics of the food

    def food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.color("Blue")
        self.speed(0)
        self.food_location()
