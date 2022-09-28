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
    
    def move(self, amount):
        self.position += amount
        if self.position < 1:
            self.position = 1

    def move_to(self, new_location):
        self.position = new_location
        if self.position < 1:
            self.position = 1