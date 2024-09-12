import time
from turtle import Screen
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    # Detect collisionw
    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Detect finish line
    if player.ycor() > FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()