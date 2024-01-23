from turtle import Turtle
from snake import snake


front = ("courier",18,"normal")
alinement = "center"

class score_bord(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('red')
        self.penup()
        self.goto(0,270)
        self.hideturtle()

#displaying the scorte

    def score_display(self):
        self.write(f"Score = {self.score} ",False,align = alinement,font = front)

#how to increment score

    def new_score(self):
        self.score += 1
        self.clear()
        self.score_display()

#how to show game over

    def game_over(self):
        self.color('red')
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.clear()
        self.write(f"Game Over\nScore = {self.score} ",False,align = "center",font = ("courier",30,"bold"))



