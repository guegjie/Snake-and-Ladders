from Window import Window
from Player import Player
from snakes_ladders import Snake, Ladder

def main():
    MainWindow = Window(Title="Snakes&Ladders")
    playerOne = Player(name="Louis", colour="red")
    playerOne.draw(MainWindow)
    
    snakeone = Snake(3, 19, MainWindow)
    snakeone.draw()
    
    MainWindow.mainloop()

if __name__ == "__main__":
    main()