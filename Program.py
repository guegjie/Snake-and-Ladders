import tkinter #imports tkinter
import math

#sheeeesh


#gridsize is the length of each part of the grid for x and y 480/48**2

class Window(tkinter.Tk): #creates a class called window  48/5=10
    def __init__(self, Title="Window", Size=[721, 481], gridsize=[48,48]): #
        super().__init__()
        self.size = Size
        self.Canvas = tkinter.Canvas(self, background="black", width=Size[0], height=Size[1])
        self.title(Title)
        self.Canvas.pack()
        self.resizable(False, False)
        print("hello world")
        self.create_grid(Gridsize=gridsize) #
        self.add_numbers(gridsize, [round(self.size[1]/gridsize[1]), round(self.size[0]/gridsize[0])], [2, 2+gridsize[1]*round(self.size[1]/gridsize[1])])
    
    def create_grid(self, Gridsize=[1,1]): # creates grid\
        for y in range(0, round(self.size[1]/Gridsize[1])):
            for x in range(0, round(self.size[0]/Gridsize[0])):
                square = [((Gridsize[0])*x+2), ((Gridsize[1])*y)+2, ((Gridsize[0]*x)+Gridsize[0])+2, ((Gridsize[1]*y)+Gridsize[0])+2] #creates the square
                self.Canvas.create_rectangle(square, fill="White")

    def add_numbers(self, square_dimensions, grid_dimensions, grid_location): #give grid_dimensions as [rows, columns], square_dimensions as [x,y], grid_location as bottom left corner of grid
        #variable determines which side the numbers count on for each row
        start_from = "left"
        #counts number
        number = 1
        #nested iteration for rows and columns in the grid
        for row in range(grid_dimensions[0]):
            #find the y value of the text using the bottom y coordinate of the grid along with the height of the squares
            y = grid_location[1] - (0.5 * square_dimensions[1]) - (square_dimensions[1] * row) #
            for square in range(grid_dimensions[1]): 
                if start_from == "left":
                    x = grid_location[0] + (0.5 * square_dimensions[0]) + (square_dimensions[0] * square)
                else:
                    right_x = grid_location[0] + (grid_dimensions[1]*square_dimensions[0])
                    x = right_x - (0.5 * square_dimensions[0]) - (square_dimensions[0] * square)
                self.Canvas.create_text(x, y, text=str(number), fill="black", font="Helvetica 8 normal")
                number += 1

            #alternates start_from from row to row
            if start_from == "left":
                start_from = "right"
            else:
                start_from = "left"

    
window = Window() #creates the object of window
window.mainloop() #run a main loop cuz i cant be bothered to program my own just yet