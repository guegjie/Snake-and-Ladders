from Window import Window
from Player import Player
from snakes_ladders import Obstacle
import random
import math


def main():
    MainWindow = Window(title="Snakes&Ladders")
    players = [Player(name="Louis", colour="red"), Player(name="Not Louis", colour="red")]
    for player in players:
        player.draw(MainWindow)
    

    snakes = []
    
    for i in range(0, round((MainWindow.total_squares/100)*4)):
        first = random.randint(16,150-16)
        second = random.randint(16,first-1)
        while first-16<=second:
            first = random.randint(16,150-16)
            second = random.randint(16,first-1)
        snakes.append(Obstacle(first, second, MainWindow, "snake"))
    
    for snake in snakes:
        snake.draw()


    ladders = []
    
    for i in range(0, round((MainWindow.total_squares/100)*4)):
        first = random.randint(16,first-1)
        second = random.randint(16,150-16)
        while first-16<=second:
            first = random.randint(16,150-16)
            second = random.randint(16,first-1)
        
        ladders.append(Obstacle(first, second, MainWindow, "ladder"))
    
    for ladder in ladders:
        ladder.draw()
    
    MainWindow.mainGameLoop(players=players)
    
    
if __name__ == "__main__":
    main()