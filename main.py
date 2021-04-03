from turtle import Screen
from slug import Slug
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Slug")

game_slug = Slug()
food = Food()
scoreboard = Scoreboard()
game_slug.start_body(5)

screen.listen()
screen.onkey(game_slug.up, "Up")
screen.onkey(game_slug.down, "Down")
screen.onkey(game_slug.left, "Left")
screen.onkey(game_slug.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.001)
    game_slug.move()

    if game_slug.body[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        game_slug.add_body()

    if game_slug.body[0].xcor() > 280 or game_slug.body[0].xcor() < -280 or game_slug.body[0].ycor() > 280 or game_slug.body[0].ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for part in game_slug.body[1:]:
        if game_slug.body[0].distance(part) < 10:
            #and part != game_slug.body[0]:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
