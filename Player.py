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
<<<<<<< HEAD
        
    def calculateBrightness(self, colour="#FFFFFF", brightness="100"):
        red = colour[1:3]
        green = colour[3:5]
        blue = colour[5:8]
        colours = [red, green, blue]
        
        for colour in colours:
            
        
        

player = Player()
player.calculateBrightness()
=======
    
    def move(self, amount):
        self.position += amount
        if self.position < 1:
            self.position = 1

    def move_to(self, new_location):
        self.position = new_location
        if self.position < 1:
            self.position = 1
>>>>>>> 4a44c140c2b3cfbb5582175b6dd6aa6ef3e90253
