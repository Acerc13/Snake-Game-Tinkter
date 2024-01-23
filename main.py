from turtle import Turtle , Screen
from snake import snake
import time
from food import food
from scorebord import score_bord


#instances ,Values and constasnts        

is_on = True
turtle = Turtle()
screen = Screen()
snake = snake()
screen.setup(width=600,height=600)
screen.bgcolor('Black')
screen.title('3310 Snake Game')
food = food()
score_bord = score_bord()



#creating a class to controle the turnd that the snake will make
class cantrole:

    def __init__(self) -> None:
        pass
    
# controle module
    def controller(self):
        screen.listen()
        if screen.onkey(snake.up,"Up"):return
        elif screen.onkey(snake.down,"Down"):return
        elif screen.onkey(snake.left,"Left"):return
        elif screen.onkey(snake.right,"Right"):return


cantrole = cantrole()   # instance of cantrole class
food.food_location()   # taking whare will the food be olaced

while is_on:   # loop to keep the game running
    
    # instances and calling modules in the loop 
    screen.update()
    time.sleep(.1)
    cantrole.controller()
    snake.move()
    score_bord.score_display()

    

  # detecting if the snaske has eten the food 
    if snake.head.distance(food) < 18 :
        food.food_location()
        score_bord.new_score()
        snake.extyend()

  # detecting collition betweeb wall and the snake
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 :
        is_on = False
        score_bord.game_over()
    else:
        is_on = True

  # detecting collition with snakes own tail
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10 :
            is_on = False
            score_bord.game_over()

    
screen.exitonclick()