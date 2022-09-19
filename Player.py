import Window
#ihioh

class Player:
    def __init__(self, name="player", position=1, colour="blue", size=[10,10]):
        self.Position = position
        self.Colour = colour

    def draw(self, window):
        window.Canvas.create_oval([window.Positions[self.Position-1][1][0]-window.gridsize[0]/2, window.Positions[self.Position-1][1][1]-window.gridsize[1]/2], [window.Positions[self.Position-1][1][0]+window.gridsize[0]/2, window.Positions[self.Position-1][1][1]+window.gridsize[1]/2], fill="red")
        