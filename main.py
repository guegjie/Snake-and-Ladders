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
    
    for i in range(0, round(((MainWindow.size[0]/MainWindow.gridsize[0]*MainWindow.size[1]/MainWindow.gridsize[1])/100)*8)):
        snakes.append(Obstacle(random.randint(16,150-16), random.randint(16,150-16), MainWindow))
    
    for snake in snakes:
        snake.draw(MainWindow)
    
    MainWindow.mainloop()

if __name__ == "__main__":
    main()