import Window
#ihioh

class Player:
    def __init__(self, name="player", position=1, colour="blue", size=[10,10]):
        self.Position = position
        self.Colour = colour

    def draw(self, window):
        coords = window.generate_coordinates(self.Position)
        
        window.Canvas.create_oval([window.Positions[self.Position-1][1][0]-window.square_size[0]/2, window.Positions[self.Position-1][1][1]-window.square_size[1]/2], [window.Positions[self.Position-1][1][0]+window.square_size[0]/2, window.Positions[self.Position-1][1][1]+window.square_size[1]/2], fill="red")
        