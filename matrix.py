from tkinter import *
import numpy as np
import time
import random

root = Tk()
root['bg'] = 'white'
root.geometry('600x600')

class Square_Matrix(Frame):
    '''
    Matrix() creates a matrix of buttons as large as needed
    '''

    def __init__(self, master, size):
        '''
        Matrix.__init__(master, size)
        master: type Simon object
        size: int: num rows and columns
        initiates the matrix
        '''

        ## initiate frame
        Frame.__init__(self, master)

        #create base matrix
        self.matrix = np.full((size, size), None)
        self.colorMatrix = np.full((size, size), None)

        # store size
        self.size = size

        #make unique colors
        self.colors = {
            'red':['#7b0000', '#ff0000'],
            'blue':['#0129bf', '#88c5fc'],
            'yellow':['#bda800', '#ffe200'],
            'green':['#137413', '#60e528'],
            'orange':['#cc5500', '#ff800d'],
            'purple':['#6b01d7', '#df00fe'],
            'brown':['#673400', '#d3b683'],
            'pink':['#AA336A', '#fe019a'],
            'turquoise':['#009896', '#99d5d5'],
            'gray': ['#454545', '#e9e9e9']
        }

        self.colorsKey = list(self.colors.keys())

        #make buttons in a loop and bind the buttons

        for row in range(size):
            for column in range(size):
                relx = column/size
                rely = row/size
                color = random.choice(self.colorsKey)

                location = (row, column)
                print(f'\n\n{color}\n\n')

                self.matrix[row, column] = Label(
                    self, 
                    bg=self.colors[color][0], 
                    borderwidth=5,
                    relief='raised'
                    )   

                self.matrix[row, column].place(
                    relx=relx,
                    rely=rely,
                    relwidth=1/size,
                    relheight=1/size
                    )
                self.matrix[row, column].bind(
                    '<Button>',
                    lambda e, loc=location: self.button_pressed(loc),
                    '+'
                    )
                
                self.colorMatrix[row, column] = color

                self.master.update()   

    def button_pressed(self, location):
        '''
        Matrix.button_pressed
        presses the button 
        returns the location of the tile
        returns int
        '''

        row, column = location
        row += 1; column += 1

        color = self.colorMatrix[row-1, column-1]

        self.matrix[row-1, column-1].configure(
            bg=self.colors[color][1],
            relief='sunken'
        )

        self.master.update()

        time.sleep(0.25)

        self.matrix[row-1, column-1].configure(
            bg=self.colors[color][0],
            relief='raised',
        )

        self.master.update()

        return location


a = Square_Matrix(root, 6)
a.pack(fill=BOTH, expand=1)

root.update()

root.mainloop()