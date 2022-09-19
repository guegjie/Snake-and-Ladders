from Window import Window
from Player import Player
from snakes_ladders import Snake, Ladder
import random

import math

def main():
    MainWindow = Window(Title="Snakes&Ladders")
    playerOne = Player(name="Louis", colour="red")
    playerOne.draw(MainWindow)


    snakes = []
    
    for i in range(0, 10):
        big = random.randint(0, 150)
        small = random.randint(0, big)
        snakes.append(Snake(small, big, MainWindow))
    
    MainWindow.mainloop()

if __name__ == "__main__":
    main()