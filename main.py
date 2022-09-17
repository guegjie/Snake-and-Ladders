import Window
import Player

def main():
    window = Window.Window()
    playerOne = Player.Player(name="Louis", colour="red")
    PlayerOne.draw(window=window)
    window.mainloop()


if __name__ == "__main__":
    main()