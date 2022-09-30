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
        
        def HexToBinary(hex="FF"):
            sum = 0
            if hex[1] == "1":
                sum += 1
                
            if hex[1] == "2":
                sum += 2
        
            if hex[1] == "3":
                sum += 3
                
            if hex[1] == "4":
                sum += 4
                
            if hex[1] == "5":
                sum += 5
            
            if hex[1] == "6":
                sum += 6
            
            if hex[1] == "7":
                sum += 7
                
            if hex[1] == "8":
                sum += 8
            
            if hex[1] == "9":
                sum += 9
            
            if hex[1] == "A":
                sum += 10
            
            if hex[1] == "B":
                sum += 11
            
            if hex[1] == "C":
                sum += 12
            
            if hex[1] == "D":
                sum += 13
            
            if hex[1] == "E":
                sum += 14
            
            if hex[1] == "F":
                sum += 15
            
            
            
            
            if hex[0] == "1":
                sum += 16
                
            if hex[0] == "2":
                sum += 32
        
            if hex[0] == "3":
                sum += 48
                
            if hex[0] == "4":
                sum += 64
                
            if hex[0] == "5":
                sum += 80
            
            if hex[0] == "6":
                sum += 96
            
            if hex[0] == "7":
                sum += 112
                
            if hex[0] == "8":
                sum += 128
            
            if hex[0] == "9":
                sum += 144
            
            if hex[0] == "A":
                sum += 160
            
            if hex[0] == "B":
                sum += 176
            
            if hex[0] == "C":
                sum += 192
            
            if hex[0] == "D":
                sum += 208
            
            if hex[0] == "E":
                sum += 224
            
            if hex[0] == "F":
                sum += 240
            
        
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
