import math

class Snake:
    def __init__(self):
        print(self.Rotate(point=[10, 10], centre=[0,0], rotation=180))
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = (point[0] * math.cos(rotation)) + (point[1] * math.sin(rotation))
        y = (point[1] * math.cos(rotation)) - (point[0] * math.sin(rotation))

        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list

    def draw(self, window):
        window.Canvas.create_polygon()
    

class Ladder:
    def __init__(self):
        pass
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = (point[0] * math.cos(rotation)) + (point[1] * math.sin(rotation))
        y = (point[1] * math.cos(rotation)) - (point[0] * math.sin(rotation))


        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list