import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()

screen.onkey(player.go_up, "Up")
count = 0
game_is_on = True
car_manager = CarManager()
scoreboard = Scoreboard()
car_manager.move()
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move()
    screen.update()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect finish line
    if player.is_on_finish_line():
        player.goto_start_position()
        scoreboard.level += 1
        scoreboard.update_scorecard()
        car_manager.level_up()


screen.exitonclick()
