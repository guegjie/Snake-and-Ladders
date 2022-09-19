from Window import Window
from Player import Player
from snakes_ladders import Obstacle
import random

import math

def main():
    MainWindow = Window(Title="Snakes&Ladders")
    playerOne = Player(name="Louis", colour="red")
    playerOne.draw(MainWindow)

    snakes = []
    
    for i in range(0, 10):
        snakes.append(Obstacle(random.randint(0,150), random.randint(0,150), MainWindow))
    
    for snake in snakes:
        print()
        snake.draw(MainWindow)
    
    MainWindow.mainloop()

if __name__ == "__main__":
    main()