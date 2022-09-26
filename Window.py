import tkinter #imports tkinter
import random

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
        self.RollBtn = tkinter.Button(self, background="white",width=10, height=1, text="Roll", command=self.rollFunc)
        self.RollBtn.pack()
        self.RollBtn.bind()
        self.grid_dimensions = [round(self.size[1]/square_size[1]), round(self.size[0]/square_size[0])]
        self.total_squares = self.grid_dimensions[1] * self.grid_dimensions[0]
        self.create_grid() #
        self.add_numbers([2, 2+square_size[1]*round(self.size[1]/square_size[1])])

    def create_grid(self): # creates grid\
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
            for square in range(self.square_size[1]): 
                if start_from == "left":
                    x = grid_location[0] + (0.5 * self.grid_dimensions[0]) + (self.grid_dimensions[0] * square)
                else:
                    right_x = grid_location[0] + (self.square_size[1]*self.square_size[0])
                    x = right_x - (0.5 * self.square_size[0]) - (self.square_size[0] * square)
                self.Canvas.create_text(x, y, text=str(number), fill="black", font="Helvetica 8 normal")
                self.Positions.append([number, [x,y]])
                number += 1

            #alternates start_from from row to row
            if start_from == "left":
                start_from = "right"
            else:
                start_from = "left"
        
    def generate_coordinates(self, number):
        return [self.Positions[number-1][1][0], self.Positions[number-1][1][1]]

    def rollFunc(self):
        print("hello world")