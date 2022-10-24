from Window import Window
from Player import Player
from snakes_ladders import Obstacle
import random
import tkinter
from tkinter import colorchooser

players = []

def startWindow():
    #Configure Window
    startWindow = tkinter.Tk()
    startWindow.title("configure Snakes&Ladders")
    startWindow.geometry("300x500")
    startWindow.resizable(False, False)
    
    #Buttons
    tkinter.Button(startWindow, text="Start", width=7, command=lambda: [startWindow.destroy(), startMain()]).pack(side=tkinter.BOTTOM)
    
    playersfield = tkinter.Canvas(startWindow, width=251, height=51, background="#a6a6a6")
    playersfield.pack(side=tkinter.BOTTOM)
    nameTextBox = tkinter.Entry(startWindow)
    nameTextBox.place(x=112, y=394, width=100, height=25)
    tkinter.Button(startWindow, text="Add", command=lambda: addPlayer("louis", playersfield)).place(x=25, y=394)
    tkinter.Button(startWindow, text="Remove", command=lambda: removePlayer(playersfield)).place(x=58, y=394)
    
    for i in range(0, len(players)):
        playersfield.create_oval([(250/5)*i+2,2], [(250/5)*(i+1)+2,52], fill=players[i].colour)
        
    #functions
    def addPlayer(name, playersfield):
        colour = colorchooser.askcolor()
        allText = nameTextBox.get()
        nameTextBox.delete(0, "end")
        if len(players) < 5 and len(allText[0]) > 0:
            players.append(Player(name=allText, colour=colour[-1]))
        else:
            print("Error Adding Player")
        
        playersfield.delete("all")
        for i in range(0, len(players)):
            playersfield.create_oval([(250/5)*i+2,2], [(250/5)*(i+1)+2,52], fill=players[i].colour)
    

    def removePlayer(playersfield):
        players.pop()
        playersfield.delete("all")
        for i in range(0, len(players)):
            playersfield.create_oval([(250/5)*i+2,2], [(250/5)*(i+1)+2,52], fill=players[i].colour)
    
    startWindow.mainloop()
    



def startMain():
    MainWindow = Window(title="Snakes&Ladders", square_size=[48, 48])
    for player in players:
        player.draw(MainWindow)
    

    snakes = []
    ladders = []


    try:
        for type in range(2):
            for i in range(0, round((MainWindow.total_squares/100)*4)):
                colliding = True
                while colliding:
                    second = random.randint(2,MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-MainWindow.grid_dimensions[1]-2)
                    first = random.randint(second + MainWindow.grid_dimensions[1], MainWindow.grid_dimensions[0]*MainWindow.grid_dimensions[1]-2)
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
    startWindow()
    
    
def main():
        startWindow()       
        



if __name__ == "__main__":
    main()