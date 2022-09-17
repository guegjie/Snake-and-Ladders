import Window
import Player

def main():
    MainWindow = Window.Window()
    playerOne = Player.Player(name="Louis", colour="red")
    playerOne.draw(window=MainWindow)
    MainWindow.mainloop()


if __name__ == "__main__":
    main()