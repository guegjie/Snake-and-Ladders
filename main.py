from csv import excel_tab
from Window import Window
from Player import Player
from snakes_ladders import Obstacle
import random
import math
import tkinter
import hello

def main():
    MainWindow = Window(title="Snakes&Ladders")
    players = [Player(name="Louis", colour="#FF0000"), Player(name="Not Louis", colour="#00FF00")]
    for player in players:
        player.draw(MainWindow)
    

    snakes = []
    
    try:
        for i in range(0, round((MainWindow.total_squares/100)*4)):
            second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
            first = random.randint(2, second-MainWindow.grid_dimensions[0])
            NotColliding = False
            while first+MainWindow.grid_dimensions[0]>=second and NotColliding:
                second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
                first = random.randint(2, second+MainWindow.grid_dimensions[0])
                for i in range(0, len(snakes)):
                    if snakes[i].end_pos == second:
                        NotCollding = False
                    
            snakes.append(Obstacle(first, second, MainWindow, "snake"))
    except:
        MainWindow.destroy()
        errorwindow = tkinter.Tk()
        errorwindow.geometry("200x100")
        Mainlabel = tkinter.Label(errorwindow, text="ERROR:001", font= ('Helvetica 25 underline'))
        errorlabel = tkinter.Label(errorwindow, text="game unable to launch due to fatal error.\n try relaunching.", font= ('Helvetica 8'))
        Mainlabel.pack()
        errorlabel.pack()
        errorwindow.mainloop()
    
    for snake in snakes:
        snake.draw()


    ladders = []
    
    try:
        for i in range(0, round((MainWindow.total_squares/100)*4)):
            second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
            first = random.randint(2, second-MainWindow.grid_dimensions[0])
            NotColliding = False
            while first+MainWindow.grid_dimensions[0]>=second and NotColliding:
                second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
                first = random.randint(2, second+MainWindow.grid_dimensions[0])
                for i in range(0, len(snakes)):
                    if ladders[i].start_pos == first:
                        NotCollding = False
            ladders.append(Obstacle(first, second, MainWindow, "ladder"))
            
    except:
        MainWindow.destroy()
        errorwindow = tkinter.Tk()
        errorwindow.geometry("200x100")
        Mainlabel = tkinter.Label(errorwindow, text="ERROR:002", font= ('Helvetica 25 underline'))
        errorlabel = tkinter.Label(errorwindow, text="game unable to launch due to fatal error.\n try relaunching.", font= ('Helvetica 8'))
        Mainlabel.pack()
        errorlabel.pack()
        errorwindow.mainloop()
    
    for ladder in ladders:
        ladder.draw()
    
    MainWindow.mainGameLoop(players=players)
    
def plus():
    print(hello.Hello())
    

if __name__ == "__main__":
    plus()