import Window
#ihioh

class Player:
    def __init__(self, name="player", position=1, colour="blue", size=[10,10]):
        self.Position = position
        self.Colour = colour

    def draw(self, window):
        coords = window.generate_coordinates(self.Position)

        window.Canvas.create_oval([coords[0]-window.square_size[0]/2, coords[1]-window.square_size[1]/2], [coords[0]+window.square_size[0]/2, coords[1]+window.square_size[1]/2], fill="red")
        
    def calculateBrightness(self, colour="#FFFFFF", brightness="100"):
        red = colour[1:3]
        green = colour[3:5]
        blue = colour[5:8]
        colours = [red, green, blue]
        
        for colour in colours:
            
        
        

player = Player()
player.calculateBrightness()