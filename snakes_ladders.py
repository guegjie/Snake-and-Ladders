import math

class Snake:
    def __init__(self, start_pos, end_pos, window):
        print(self.Rotate(point=[10, 10], centre=[0,0], rotation=180))
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.window = window
        self.generate_snake()
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = (point[0] * math.cos(rotation)) + (point[1] * math.sin(rotation))
        y = (point[1] * math.cos(rotation)) - (point[0] * math.sin(rotation))


        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list

    def generate_coordinates(self, number):
        #variable determines which side the numbers count on for each row
        start_from = "left"        


    def generate_snake(self):
        start_point = self.start_point
        end_point = self.end_point
        length = math.sqrt(((start_pos[0]-end_pos[0])**2) + ((start_pos[1]-end_pos[1]) ** 2))
        #head
        points = [[start_point[0] + 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 2.5], start_point, [start_point[0] + 5, start_point[1] + 2.5], [start_point[0] + 5, start_point[1] + 7.5]]
        #body
        points_2 = [start_point[0] + 2.5, start_point[1] + 7.5], [start_point[0] + 2.5, start_point[1] + length - 2.5], [start_point[0], start_point[1] + length], [start_point[0] - 2.5, start_point[1] + length - 2.5], [start_point[0] - 2.5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5]

        points = points + points_2

        angle = math.acos((start_point[1]-end_point[1])/length)

        points_rotated = []
        for point in points:
            points_rotated.append(self.Rotate(point, start_point, angle))

        self.points = points_rotated

    def draw(self):
        self.window.Canvas.create_polygon(self.points, fill="black")
    

class Ladder:
    def __init__(self):
        pass
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = (point[0] * math.cos(rotation)) + (point[1] * math.sin(rotation))
        y = (point[1] * math.cos(rotation)) - (point[0] * math.sin(rotation))


        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list