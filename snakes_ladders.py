import math

class Obstacle:
    def __init__(self, start_pos, end_pos, window, type="snake"):
        print(self.Rotate(point=[10, 10], centre=[0,0], rotation=180))
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.start_coords = window.generate_coordinates(start_pos)
        self.end_coords = window.generate_coordinates(end_pos)
        self.type = type
        if self.type == "snake":
            self.generate_snake()
        if self.type == "ladder":
            pass
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = ((point[0]-centre[0]) * math.cos(rotation)) + ((point[1]-centre[1]) * math.sin(rotation))
        y = ((point[1]-centre[1]) * math.cos(rotation)) - ((point[0]-centre[0]) * math.sin(rotation))

        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list

    def rotate(self, point, origin, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.

        The angle should be given in radians.
        """
        angle = math.radians(angle)
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return [qx, qy]

    def generate_snake(self):
        if self.start_coords < self.end_coords:
            start_point = self.start_coords
            end_point = self.end_coords
        else:
            start_point = self.end_coords
            end_point = self.start_coords
        print(start_point)
        print(end_point)
        length = math.sqrt(((start_point[0]-end_point[0])**2) + ((start_point[1]-end_point[1]) ** 2))

        #head
        #points = [[start_point[0] + 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 2.5], start_point, [start_point[0] + 5, start_point[1] + 2.5], [start_point[0] + 5, start_point[1] + 7.5]]
        #body
        #points.extend([[start_point[0] + 2.5, start_point[1] + 7.5], [start_point[0] + 2.5, start_point[1] + length - 2.5], [start_point[0], start_point[1] + length], [start_point[0] - 2.5, start_point[1] + length - 2.5], [start_point[0] - 2.5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5]])
        points = [[start_point[0] - 2.5, start_point[1]], [start_point[0] + 2.5, start_point[1]], [start_point[0] + 2.5, start_point[1] + length], [start_point[0] - 2.5, start_point[1]+length]]


        print(points)

        vector_right = [1,0]
        vector_points = [end_point[0]-start_point[0], end_point[1]-start_point[1]]

        angle = math.acos(vector_points[0] / math.sqrt((vector_points[0]**2)+(vector_points[1]**2)))

        #thing_in_cos = abs(start_point[0]-end_point[0]) / length
        
        #angle = math.acos(abs(start_point[1]-end_point[1]) / length)
        #angle = math.acos(thing_in_cos)
        angle = math.degrees(angle)
        #print(thing_in_cos)
        #print(angle)
        #angle = angle + 90
        #if angle >= 180:
            #angle = 270 - angle


        points_rotated = []
        for point in points:
            points_rotated.append(self.Rotate(point, start_point, 90 + angle))

        self.points = points_rotated
        print(self.points)


    def draw(self, window):
        window.Canvas.create_polygon(self.points, fill="black")
    
