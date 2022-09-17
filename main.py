import Window
import Player

def main():
    window = Window.Window()
    playerOne = Player.Player(name="Louis", colour="red")
    playerOne.draw(window=window)
    window.mainloop()


if __name__ == "__main__":
    main()