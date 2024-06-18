from tkinter import *
import numpy as np
import time
import random

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
        #list index 0: color when not pressed
        #list index 1: color when pressed
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

                #make sure the matrix completely fits in the frame
                relx = column/size
                rely = row/size

                #choose a unique color about every time
                color = random.choice(self.colorsKey)

                #set location

                location = (row, column)

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

        self.lastButton = ()   

    def button_pressed(self, location):
        '''
        Matrix.button_pressed
        presses the button 
        returns the location of the tile
        returns None
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

        self.lastButton = location
