from http.client import NOT_EXTENDED
from pickle import NONE
import tkinter #imports tkinter
import random
import time
import math

#afiahoi
#gridsize is the length of each part of the grid for x and y 480/48**2

class Window(tkinter.Tk): #creates a class called window  48/5=10
    def __init__(self, title="Window", size=[721, 481], square_size=[48,48]):
        super().__init__()
        self.title(title)
        self.size = size
        self.square_size = square_size
        self.Positions = []
        self.resizable(False, False)
        self.Canvas = tkinter.Canvas(self, background="black", width=size[0], height=size[1])
        self.Canvas.pack()
        self.turn = 0
        self.RollBtn = tkinter.Button(self, background="white",width=10, height=1, text="Roll", command=self.rollFunc)
        self.RollBtn.pack()
        self.grid_dimensions = [round(self.size[1]/self.square_size[1]), round(self.size[0]/self.square_size[0])]
        self.total_squares = self.grid_dimensions[1] * self.grid_dimensions[0]
        self.create_grid() #
        self.add_numbers([2, 2+square_size[1]*round(self.size[1]/square_size[1])])
        self.roll_label = None
        self.call('wm', 'iconphoto', self._w, tkinter.PhotoImage(file='Icon.png'))

    def create_grid(self): # creates grid
        for y in range(0, self.grid_dimensions[0]):
            for x in range(0, self.grid_dimensions[1]):
                square = [((self.square_size[0])*x+2), ((self.square_size[1])*y)+2, ((self.square_size[0]*x)+self.square_size[0])+2, ((self.square_size[1]*y)+self.square_size[0])+2] #creates the square
                self.Canvas.create_rectangle(square, fill="White")

    def add_numbers(self, grid_location): #give grid_dimensions as [rows, columns], square_dimensions as [x,y], grid_location as bottom left corner of grid
        #variable determines which side the numbers count on for each row
        start_from = "left"
        #counts number
        number = 1
        #nested iteration for rows and columns in the grid
        for row in range(self.grid_dimensions[0]):
            #find the y value of the text using the bottom y coordinate of the grid along with the height of the squares
            y = grid_location[1] - (0.5 * self.square_size[1]) - (self.square_size[1] * row) #
            for square in range(self.grid_dimensions[1]): 
                if start_from == "left":
                    x = grid_location[0] + (0.5 * self.square_size[0]) + (self.square_size[0] * square)
                else:
                    right_x = grid_location[0] + (self.grid_dimensions[1]*self.square_size[0])
                    x = right_x - (0.5 * self.square_size[0]) - (self.square_size[0] * square)
                self.Canvas.create_text(x, y, text=str(number), fill="black", font="Helvetica 8 normal")
                self.Positions.append([number, [x,y]])
                number += 1

            #alternates start_from from row to row
            if start_from == "left":
                start_from = "right"
            else:
                start_from = "left"

    def create_end_star(self):
        def add_vectors(vectors=[]):
            sum = [0,0]
            for vector in vectors:
                sum[0] += vector[0]
                sum[1] += vector[1]
            return sum

        end_pos = self.grid_dimensions[0] * self.grid_dimensions[1]
        end_coords = self.generate_coordinates(end_pos)
        x = self.square_size[0]
        y = self.square_size[1]
        point1 = add_vectors([end_coords, [0, -0.5*y], [-0.5*x,0], [0,x-(math.cos(18)*x*math.sin(36)/math.sin(108))]])
        points = [[end_coords[0], end_coords[1]-self.square_size[1]]] 
        self.window.create_polygon(points, fill="yellow")
        
    def generate_coordinates(self, number):
        return [self.Positions[number-1][1][0], self.Positions[number-1][1][1]]
    
    def detect_collision(self, player, obstacles):
        step = self.square_size[0]
        player_coords = self.generate_coordinates(player.position)
        obstacle_collided = NONE
        for obstacle in obstacles:
            if obstacle.start_pos == player.position:
                print("collided")
                obstacle_collided = obstacle
        if obstacle_collided != NONE:
            for i in range(int(obstacle_collided.length/step)):
                player_coords[0] += obstacle_collided.unit_vector[0] * step
                player_coords[1] += obstacle_collided.unit_vector[1] * step
                player.undraw(self)
                player.draw_coords(self, player_coords)
                self.update()
                time.sleep(0.016)
            player.position = obstacle_collided.end_pos


    def mainGameLoop(self, players=[], obstacles = []):
        print(obstacles)
        running = True
        self.turn = 0
        turn_player = NONE
        self.total_roll = 0
            
        while running:
            for player in players:
                player.undraw(self)
                
            for player in players:
                player.draw(self)
                
            if self.turn >= len(players):
                self.turn = 0
            
            for i in range(0, len(players)):
                if self.turn == i:
                    turn_player = players[i-1]
                    players[i].brightness = int(round(math.cos(math.radians(players[i].step)) * 25 + 75))
                    #players[i].brightness = 50
                    players[i].step += 10
                        
                    for r in range(0, self.total_roll):
                        players[i-1].undraw(self)
                        players[i-1].position += 1
                        players[i-1].draw(self)
                        self.update()
                        time.sleep(0.016)
                    self.total_roll = 0
                    self.detect_collision(players[i-1], obstacles)
                
                if self.turn != i:
                    players[i].brightness = 100
                    players[i].step = 0
            

            self.update()
            time.sleep(0.016)

    def rollFunc(self):
        if self.roll_label != None:
            self.roll_label.destroy()
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        self.total_roll = roll1 + roll2
        self.roll_label = tkinter.Label(self, text="You rolled a {0} and a {1}.".format(roll1, roll2))
        self.roll_label.pack()
        self.turn += 1