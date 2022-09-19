from Window import Window
from Player import Player
from snakes_ladders import Snake, Ladder

import math

def main():
    MainWindow = Window(Title="Snakes&Ladders")
    playerOne = Player(name="Louis", colour="red")
    playerOne.draw(MainWindow)
    
    snakeone = Snake(97, 3, MainWindow)
    snakeone.draw(MainWindow)
    
    MainWindow.mainloop()

if __name__ == "__main__":
    main()