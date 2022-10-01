from binhex import hexbin
import Window
import tkinter
#ihioh

class Player:
    def __init__(self, name="player", position=1, colour="#FFFFFF", size=[10,10]):
        self.position = position
        self.colour = colour
        self.size = size
        self.brightness = 100
        self.step = 0

    def draw(self, window):
        try:
            coords = window.generate_coordinates(self.position)
            radius = self.size[0] / 2
            self.drawnplayer = window.Canvas.create_oval([coords[0]-window.square_size[0]/2, coords[1]-window.square_size[1]/2], [coords[0]+window.square_size[0]/2, coords[1]+window.square_size[1]/2], fill=self.calculateBrightness(self.colour, self.brightness))
        except:
            window.destroy()
            errorwindow = tkinter.Tk()
            errorwindow.geometry("200x100")
            errorwindow.title("Error")
            errorwindow.iconbitmap("Icons\Error.ico")
            Mainlabel = tkinter.Label(errorwindow, text="ERROR:003", font= ('Helvetica 25 underline'))
            errorlabel = tkinter.Label(errorwindow, text="game unable to draw player due to fatal\n error.", font= ('Helvetica 8'))
            Mainlabel.pack()
            errorlabel.pack()
            errorwindow.mainloop()
            
    def undraw(self, window):
        window.Canvas.delete(self.drawnplayer)
    
    def calculateBrightness(self, colour="#FFFFFF", brightness="100"):
        red = colour[1:3]
        green = colour[3:5]
        blue = colour[5:8]
        colours = [red, green, blue]
        
        def HexToBinary(hex):
            return int(hex, 16)
            
        
        colourButInDenary = [HexToBinary(colours[0]), HexToBinary(colours[1]), HexToBinary(colours[2])]
        colourButInDenary[0] = (colourButInDenary[0]/100)*brightness
        colourButInDenary[1] = (colourButInDenary[1]/100)*brightness
        colourButInDenary[2] = (colourButInDenary[2]/100)*brightness
        
        Hex = "#" + hex(round(colourButInDenary[0]))[2:3] + hex(round(colourButInDenary[1]))[2:3] + hex(round(colourButInDenary[2]))[2:3]
        return Hex
        
    def move(self, amount):
        self.position += amount
        if self.position < 1:
            self.position = 1

    def move_to(self, new_location):
        self.position = new_location
        if self.position < 1:
            self.position = 1
