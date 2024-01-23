from turtle import Turtle , Screen
import time


UP = 90
DOWN = 270
LEFT = 180 
RIGHT = 0


class snake:

    def __init__(self) -> None:
        self.position = [(0,0),(-20,0),(-40,0)]
        self.travle_distence = 20
        self.screen = Screen()
        self.segments = []
        self.create()
        self.head = self.segments[0]

#creating the snake blocks

    def create(self):
        self.screen.tracer(0)
        for i in self.position:
            self.add_segment(i)

# adding segments to the snake

    def add_segment(self,position):
        body_block = Turtle()
        self.segments.append(body_block)
        body_block.penup()
        body_block.shape("square")
        body_block.shapesize(.70,.70,5)
        body_block.color('white')
        body_block.setposition(position)
        print(self.segments)

# whare to add the segments to
        
    def extyend(self):
        self.add_segment(self.segments[-1].position())

#movement of the  snake 

    def move(self):

        for seg in range (((len(self.segments)) - 1), 0 ,-1):
            x_cd = self.segments[seg-1].xcor()
            y_cd = self.segments[seg-1].ycor()
            self.segments[seg].goto(x_cd,y_cd)
        self.head.forward(self.travle_distence)

    def up(self):
        if self.head.heading() == 270 :
            return 0
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == 90 :
            return 0
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == 0 :
            return 0
        else:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == 180 :
            return 0
        else:
            self.head.setheading(RIGHT)

    