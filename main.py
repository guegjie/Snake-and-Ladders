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

        # for i in range(0, round((MainWindow.total_squares/100)*4)):
        #     second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
        #     first = random.randint(2, second+MainWindow.grid_dimensions[0])
        #     NotColliding = False
        #     while first+MainWindow.grid_dimensions[0]>=second and NotColliding:
        #         second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
        #         first = random.randint(2, second+MainWindow.grid_dimensions[0])
        #         for i in range(0, len(snakes)):
        #             if snakes[i].end_pos == second:
        #                 NotColliding = False

        #     snakes.append(Obstacle(first, second, MainWindow, "snake"))

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


    
        # for i in range(0, round((MainWindow.total_squares/100)*4)):
        #     second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
        #     first = random.randint(2, MainWindow.grid_dimensions[0]-second)
        #     NotColliding = True
        #     while first+MainWindow.grid_dimensions[0]>=second and NotColliding:
        #         second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
        #         first = random.randint(2, second+MainWindow.grid_dimensions[0])
        #         for i in range(0, len(ladders)):
        #             if ladders[i].start_pos == first:
        #                 NotColliding = False
        #     ladders.append(Obstacle(first, second, MainWindow, "ladder"))
            
    # for i in range(0, round((MainWindow.total_squares/100)*4)):
    #     first = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-MainWindow.grid_dimensions[1])
    #     second = random.randint(first + MainWindow.grid_dimensions[1], MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1])
    #     colliding = True
    #     while colliding:
    #         first = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-MainWindow.grid_dimensions[1])
    #         second = random.randint(first + MainWindow.grid_dimensions[1], MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1])
    #         colliding = False
    #         for i in range(0, len(ladders)):
    #             if ladders[i].end_pos == second:
    #                 colliding = True

    #     ladders.append(Obstacle(first, second, MainWindow, "ladder"))

    # except:
    #     MainWindow.destroy()
    #     errorwindow = tkinter.Tk()
    #     errorwindow.geometry("200x100")
    #     errorwindow.title("Error")
    #     errorIcon = tkinter.PhotoImage("Icons\Error.png")
    #     errorwindow.iconbitmap(errorIcon)
    #     Mainlabel = tkinter.Label(errorwindow, text="ERROR:002", font= ('Helvetica 25 underline'))
    #     errorlabel = tkinter.Label(errorwindow, text="game unable to launch due to fatal error.\n try relaunching.", font= ('Helvetica 8'))
    #     Mainlabel.pack()
    #     errorlabel.pack()
    #     errorwindow.mainloop()
    
    for ladder in ladders:
        ladder.draw()
    
    MainWindow.mainGameLoop(players=players)
    
    

if __name__ == "__main__":
    main()