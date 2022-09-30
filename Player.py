from binhex import hexbin
import Window
#ihioh

class Player:
    def __init__(self, name="player", position=1, colour="blue", size=[10,10]):
        self.position = position
        self.colour = colour
        self.size = size

    def draw(self, window):
        coords = window.generate_coordinates(self.position)
        radius = self.size[0] / 2
        window.Canvas.create_oval([coords[0]-window.square_size[0]/2, coords[1]-window.square_size[1]/2], [coords[0]+window.square_size[0]/2, coords[1]+window.square_size[1]/2], fill="red")
        
    def calculateBrightness(self, colour="#FFFFFF", brightness="100"):
        red = colour[1:3]
        green = colour[3:5]
        blue = colour[5:8]
        colours = [red, green, blue]
        
        def HexToBinary(hex):
            return int(hex, 16)
            
        
        colourButInDenary = [HexToBinary(colour[0]), HexToBinary(colour[1]), HexToBinary(colour[2])]
        colourButInDenary[0] = (colourButInDenary[0]/100)*brightness
        colourButInDenary[1] = (colourButInDenary[1]/100)*brightness
        colourButInDenary[2] = (colourButInDenary[2]/100)*brightness
        
        Hex = "#" + hex(colourButInDenary[0]) + hex(colourButInDenary[1]) + hex(colourButInDenary[2])
        return Hex
        
    def move(self, amount):
        self.position += amount
        if self.position < 1:
            self.position = 1

    def move_to(self, new_location):
        self.position = new_location
        if self.position < 1:
            self.position = 1
