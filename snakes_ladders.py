import math

class Obstacle:
    def __init__(self, start_pos, end_pos, window, type="snake"):
        self.start_pos = start_pos
        self.end_pos = end_pos
        print(self.start_pos, self.end_pos)
        self.window = window
        self.start_coords = self.window.generate_coordinates(start_pos)
        self.end_coords = self.window.generate_coordinates(end_pos)
        self.type = type
        self.generate_obstacle()
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = ((point[0]-centre[0]) * math.cos(rotation)) + ((point[1]-centre[1]) * math.sin(rotation))
        y = ((point[1]-centre[1]) * math.cos(rotation)) - ((point[0]-centre[0]) * math.sin(rotation))

        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list


    def generate_obstacle(self):
        if self.start_coords < self.end_coords:
            start_point = self.start_coords
            end_point = self.end_coords
        else:
            start_point = self.end_coords
            end_point = self.start_coords

        self.window.Canvas.create_oval(start_point[0] - 2, start_point[1] - 2, start_point[0] + 2, start_point[1] + 2, fill="green")
        self.window.Canvas.create_oval(end_point[0] - 2, end_point[1] - 2, end_point[0] + 2, end_point[1] + 2, fill="red")
        
        length = math.sqrt(((start_point[0]-end_point[0])**2) + ((start_point[1]-end_point[1]) ** 2))

        if self.type == "snake":
            #head
            #points = [[start_point[0] + 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 2.5], start_point, [start_point[0] + 5, start_point[1] + 2.5], [start_point[0] + 5, start_point[1] + 7.5]]
            #body
            #points.extend([[start_point[0] + 2.5, start_point[1] + 7.5], [start_point[0] + 2.5, start_point[1] + length - 2.5], [start_point[0], start_point[1] + length], [start_point[0] - 2.5, start_point[1] + length - 2.5], [start_point[0] - 2.5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5]])
            points = [[start_point[0] - 2.5, start_point[1]], [start_point[0] + 2.5, start_point[1]], [start_point[0] + 2.5, start_point[1] + length], [start_point[0] - 2.5, start_point[1]+length]]

        if self.type == "ladder":
            pass

        vector_right = [1,0]
        vector_points = [end_point[0]-start_point[0], end_point[1]-start_point[1]]

        angle = math.acos(vector_points[0] / math.sqrt((vector_points[0]**2)+(vector_points[1]**2)))
        angle = math.degrees(angle)

        points_rotated = []
        for point in points:
            points_rotated.append(self.Rotate(point, start_point, 90 + angle))

        self.points = points_rotated


    def draw(self):
        self.window.Canvas.create_polygon(self.points, fill="black")
    
