from csv import excel_tab
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
    
    try:
        for i in range(0, round((MainWindow.total_squares/100)*4)):
            first = random.randint(16,150-16)
            second = random.randint(16,first-1)
            while first-16<=second:
                first = random.randint(16,150-16)
                second = random.randint(16,first-1)
            snakes.append(Obstacle(first, second, MainWindow, "snake"))
    except:
        MainWindow.destroy()
        errorwindow = tkinter.Tk()
        errorwindow.geometry("200x100")
        Mainlabel = tkinter.Label(errorwindow, text="ERROR:001", font= ('Helvetica 25 underline'))
        errorlabel = tkinter.Label(errorwindow, text="game unable to launch due to fatal error. try relaunching.", font= ('Helvetica 8'))
        Mainlabel.pack()
        errorlabel.pack()
        errorwindow.mainloop()
    
    for snake in snakes:
        snake.draw()


    ladders = []
    
    try:
        for i in range(0, round((MainWindow.total_squares/100)*4)):
            first = random.randint(16,first-1)
            second = random.randint(16,150-16)
            while first-16<=second:
                first = random.randint(16,150-16)
                second = random.randint(16,first-1)
        
            ladders.append(Obstacle(first, second, MainWindow, "ladder"))
    except:
        MainWindow.destroy()
        errorwindow = tkinter.Tk()
        errorwindow.geometry("200x100")
        Mainlabel = tkinter.Label(errorwindow, text="ERROR:002", font= ('Helvetica 25 underline'))
        errorlabel = tkinter.Label(errorwindow, text="game unable to launch due to fatal error. try relaunching.", font= ('Helvetica 8'))
        Mainlabel.pack()
        errorlabel.pack()
        errorwindow.mainloop()
    
    for ladder in ladders:
        ladder.draw()
    
    MainWindow.mainGameLoop(players=players)
    
    
if __name__ == "__main__":
    main()