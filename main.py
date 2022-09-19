from Window import Window
import Player

def main():
    MainWindow = Window(Title="Snakes&Ladders")
    playerOne = Player.Player(name="Louis", colour="red")
    playerOne.draw(MainWindow)
    MainWindow.mainloop()

if __name__ == "__main__":
    main()