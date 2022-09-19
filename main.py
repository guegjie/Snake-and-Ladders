from Window import Window
from Player import Player
from snakes_ladders import Snake, Ladder

import math

def main():
    MainWindow = Window(Title="Snakes&Ladders")
    playerOne = Player(name="Louis", colour="red")
    playerOne.draw(MainWindow)
    
<<<<<<< HEAD
    snakeone = Snake(3, 97, MainWindow)
=======
    snakeone = Snake(97, 3, MainWindow)
>>>>>>> c52cb58269fda916f8a65eb130690eb1e68b1f8b
    snakeone.draw(MainWindow)
    
    MainWindow.mainloop()

if __name__ == "__main__":
    main()