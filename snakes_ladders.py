import math
from weakref import finalize

class Obstacle:
    def __init__(self, start_pos, end_pos, window, type="snake"):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.type = type
        if (self.type == "snake" and self.start_pos < self.end_pos) or (self.type == "ladder" and self.start_pos > self.end_pos):
            temp = self.start_pos
            self.start_pos = self.end_pos
            self.end_pos = temp
        print(self.start_pos, self.end_pos)
        self.window = window
        self.start_coords = self.window.generate_coordinates(start_pos)
        self.end_coords = self.window.generate_coordinates(end_pos)
        self.vector = [self.end_coords[0]-self.start_coords[0], self.end_coords[1]-self.start_coords[1]]
        self.length = math.sqrt((self.vector[0]**2)+(self.vector[1]**2))
        self.unit_vector = [self.vector[0]/self.length, self.vector[1]/self.length]
        self.generate_obstacle()
    
    def Rotate(self, point=[0,0], centre=[0,0], rotation=0):
        rotation = math.radians(rotation)

        x = ((point[0]-centre[0]) * math.cos(rotation)) + ((point[1]-centre[1]) * math.sin(rotation))
        y = ((point[1]-centre[1]) * math.cos(rotation)) - ((point[0]-centre[0]) * math.sin(rotation))

        point_list = [round(x + centre[0]), round(y + centre[1])]
        return point_list


    def generate_obstacle(self):
        if self.start_pos < self.end_pos:
            start_point = self.start_coords
            end_point = self.end_coords
        else:
            start_point = self.end_coords
            end_point = self.start_coords

        #self.window.Canvas.create_oval(start_point[0] - 5, start_point[1] - 5, start_point[0] + 5, start_point[1] + 5, fill="green")
        #self.window.Canvas.create_oval(end_point[0] - 5, end_point[1] - 5, end_point[0] + 5, end_point[1] + 5, fill="red")
        
        length = math.sqrt(((start_point[0]-end_point[0])**2) + ((start_point[1]-end_point[1]) ** 2))

        if self.type == "snake":
            #head
            #points = [[start_point[0] + 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 2.5], start_point, [start_point[0] + 5, start_point[1] + 2.5], [start_point[0] + 5, start_point[1] + 7.5]]
            #body
            #points.extend([[start_point[0] + 2.5, start_point[1] + 7.5], [start_point[0] + 2.5, start_point[1] + length - 2.5], [start_point[0], start_point[1] + length], [start_point[0] - 2.5, start_point[1] + length - 2.5], [start_point[0] - 2.5, start_point[1] + 7.5], [start_point[0] - 5, start_point[1] + 7.5]])
            #points = [[start_point[0] - 2.5, start_point[1]], [start_point[0] + 2.5, start_point[1]], [start_point[0] + 2.5, start_point[1] + length], [start_point[0] - 2.5, start_point[1]+length]]
            
            body=[]
            sectionLength = 10
            head = [[start_point[0], start_point[1]+length+self.window.square_size[1]/8], [start_point[0]+self.window.square_size[0]/5, start_point[1]+length-self.window.square_size[1]/4], [start_point[0], start_point[1]+length-self.window.square_size[1]/2], [start_point[0]-self.window.square_size[0]/5, start_point[1]+length-self.window.square_size[1]/4]]
            for i in range(0, round(length), round(length/sectionLength)):
                body.append([[start_point[0]-sectionLength, start_point[1]+length-self.window.square_size[1]/2-sectionLength]])
            self.points = self.finalPoints(end_point, start_point, head)
            self.points2 = self.multifinalPoints(end_point, start_point, body)
            
        
        
        thicknessFraction = 15
        sizeFraction = 4
        distanceBetweenHandles = 20
        points3=[]
        
        
        if self.type == "ladder":
            points = [[start_point[0] - self.window.square_size[0]/sizeFraction + self.window.square_size[0]/thicknessFraction, start_point[1]], [start_point[0] - self.window.square_size[0]/sizeFraction, start_point[1]], [start_point[0] - self.window.square_size[0]/sizeFraction, start_point[1] + length], [start_point[0] - self.window.square_size[0]/sizeFraction + self.window.square_size[0]/thicknessFraction, start_point[1]+length]]
            points2 = [[start_point[0] + self.window.square_size[0]/sizeFraction - self.window.square_size[0]/thicknessFraction, start_point[1]], [start_point[0] + self.window.square_size[0]/sizeFraction, start_point[1]], [start_point[0] + self.window.square_size[0]/sizeFraction, start_point[1] + length], [start_point[0] + self.window.square_size[0]/sizeFraction - self.window.square_size[0]/thicknessFraction, start_point[1]+length]]
            for i in range(distanceBetweenHandles, round(length-distanceBetweenHandles), distanceBetweenHandles):
                points3.append([[start_point[0] + self.window.square_size[0]/sizeFraction - self.window.square_size[0]/thicknessFraction, start_point[1]+i], [start_point[0] - self.window.square_size[0]/sizeFraction + self.window.square_size[0]/thicknessFraction, start_point[1]+i], [start_point[0] - self.window.square_size[0]/sizeFraction + self.window.square_size[0]/thicknessFraction, start_point[1]+i+self.window.square_size[1]/thicknessFraction], [start_point[0] + self.window.square_size[0]/sizeFraction - self.window.square_size[0]/thicknessFraction, start_point[1]+i+self.window.square_size[1]/thicknessFraction]])
            self.points = self.finalPoints(end_point, start_point, points)
            self.points2 = self.finalPoints(end_point, start_point, points2)
            self.points3 = self.multifinalPoints(end_point, start_point, points3)
    
    
    
    def finalPoints(self, end_point, start_point, points):
        vector_points = [end_point[0]-start_point[0], end_point[1]-start_point[1]]

        angle = math.acos(vector_points[0] / self.length)
        angle = math.degrees(angle)

        points_rotated = []
        for point in points:
            points_rotated.append(self.Rotate(point, start_point, 90 + angle))

        return points_rotated


    def multifinalPoints(self, end_point, start_point, pointss):
        vector_points = [end_point[0]-start_point[0], end_point[1]-start_point[1]]

        angle = math.acos(vector_points[0] / self.length)
        angle = math.degrees(angle)

        points_rotated = []
        for points in pointss:
            for point in points:
                points_rotated.append(self.Rotate(point, start_point, 90 + angle))

        return points_rotated


    def draw(self):
        if self.type == "snake":
            self.window.Canvas.create_polygon(self.points, fill="green", outline="black")
            self.window.Canvas.create_polygon(self.points2, fill="green", outline="black")
        if self.type == "ladder":
            self.window.Canvas.create_polygon(self.points, fill="brown", outline="black")
            self.window.Canvas.create_polygon(self.points2, fill="brown", outline="black")
            self.window.Canvas.create_polygon(self.points3, fill="brown", outline="black")