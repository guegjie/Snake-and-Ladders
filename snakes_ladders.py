import math

class Snake:
    def __init__(self, start_pos, end_pos):
        print(self.Rotate(point=[10, 10], centre=[0,0], rotation=180))
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.start_coords = self.window.generate_coordinates(start_pos)
        self.end_coords = self.window.generate_coordinates(end_pos)
        self.generate_snake()
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = (point[0] * math.cos(rotation)) + (point[1] * math.sin(rotation))
        y = (point[1] * math.cos(rotation)) - (point[0] * math.sin(rotation))

        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list

    def generate_snake(self):
        start_point = self.start_coords
        end_point = self.end_coords
        length = math.sqrt(((start_point[0]-end_point[0])**2) + ((start_point[1]-end_point[1]) ** 2))
        #head
        points = [[start_point[0] + 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 2.5], start_point, [start_point[0] + 5, start_point[1] + 2.5], [start_point[0] + 5, start_point[1] + 7.5]]
        #body
        points.extend([[start_point[0] + 2.5, start_point[1] + 7.5], [start_point[0] + 2.5, start_point[1] + length - 2.5], [start_point[0], start_point[1] + length], [start_point[0] - 2.5, start_point[1] + length - 2.5], [start_point[0] - 2.5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5]])

        angle = math.acos((start_point[1]-end_point[1])/length)

        points_rotated = []
        for point in points:
            points_rotated.append(self.Rotate(point, start_point, 180+angle))

        self.points = points_rotated
        print(self.points)


    def draw(self, window):
        window.Canvas.create_polygon(self.points, fill="black")
    

class Ladder:
    def __init__(self):
        pass
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = (point[0] * math.cos(rotation)) + (point[1] * math.sin(rotation))
        y = (point[1] * math.cos(rotation)) - (point[0] * math.sin(rotation))


        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list