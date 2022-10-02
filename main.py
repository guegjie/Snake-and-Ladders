from Window import Window
from Player import Player
from snakes_ladders import Obstacle
import random
import math
import tkinter

def main():
    MainWindow = Window(title="Snakes&Ladders")
    players = [Player(name="Louis", colour="#FF0000"), Player(name="Not Louis", colour="#00FF00")]
    for player in players:
        player.draw(MainWindow)
    

    snakes = []
    ladders = []


    try:
        for type in range(2):
            for i in range(0, round((MainWindow.total_squares/100)*4)):
                colliding = True
                while colliding:
                    second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-MainWindow.grid_dimensions[1])
                    first = random.randint(second + MainWindow.grid_dimensions[1], MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1])
                    if type == 1:
                        temp = second
                        second = first
                        first = temp
                    colliding = False
                    for i in range(0, len(snakes)):
                        if snakes[i].start_pos == first:
                            colliding = True
                    for i in range(0, len(ladders)):
                        if ladders[i].start_pos == first:
                            colliding = True
                if type == 0:
                    snakes.append(Obstacle(first, second, MainWindow, "snake"))
                else:
                    ladders.append(Obstacle(first, second, MainWindow, "ladder"))
                    

    except:
        MainWindow.destroy()
        errorwindow = tkinter.Tk()
        errorwindow.geometry("200x100")
        errorwindow.title("Error")
        errorwindow.call('wm', 'iconphoto', errorwindow._w, tkinter.PhotoImage(file='Error.png'))
        Mainlabel = tkinter.Label(errorwindow, text="ERROR:001", font= ('Helvetica 25 underline'))
        errorlabel = tkinter.Label(errorwindow, text="game unable to launch due to fatal error.\n try relaunching.", font= ('Helvetica 8'))
        Mainlabel.pack()
        errorlabel.pack()
        errorwindow.mainloop()
    

    
    for snake in snakes:
        snake.draw()

    
    for ladder in ladders:
        ladder.draw()
    
    MainWindow.mainGameLoop(players=players, obstacles=snakes+ladders)
    
    

if __name__ == "__main__":
    main()