from matrix import *
import sys

sys.path.append('/Users/anayaahanotu/Coding/GitHub/')

from Special_tkinter_objects import tkinterPlus2 as tk2


root = Tk()
root.geometry('600x600')
root['bg'] = '#FFFFF0'

class MegaSimon(Frame):
    '''
    Mega Simon! Plays a game of Mega Simon!
    '''

    def __init__(self, master):
        '''
        MegaSimon(master)
        master: tkinter.Tk or tkinter.Frame
        creates Mega Simon
        '''

        self.master = master
    
        Frame.__init__(self, master, bg = self.master['bg'])
        self.pack(fill='both', expand=1)


        self.font = ['American Typewriter']

        self.title = Label(
            self,
            text='Simon!',
            bg='white',
            fg='black',
            font=self.font + [60, 'bold']
        )

        self.title.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1, anchor='n')

        self.scoreLabel = Label(
            self,
            text='Score: 0',
            fg='black',
            bg='white',
            font=self.font + [12],
            relief='groove',
            borderwidth=3
        )

        self.scoreLabel.place(relx=0, rely=0, relwidth=0.25, relheight=0.05)

        self.highScoreLabel = Label(
            self,
            text='High Score: 0',
            fg='black',
            bg='white',
            font=self.font + [12],
            relief='groove',
            borderwidth=3
        )

        self.highScoreLabel.place(relx=0, rely=0.05, relwidth=0.25, relheight=0.05)

        self.computer_sequence = []
        self.player_sequence = []

        self.playerTurn = False
        self.playerWinning = None

        self.setup()




    def setup(self):

    #create temporary Frame

    #make function to set up matrix

        def begin(oldFrame, size):
            size = list(item for item in size if item.isnumeric())
            size = size[:len(size)//2]

            matrixSize = ''

            for element in size: matrixSize += element

            matrixSize = int(matrixSize)

            self.matrix = Square_Matrix(self, matrixSize)
            self.matrix.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)

            print(size)

        temporaryFrame = Frame(
            self,
            bg=self['bg']
        )
        temporaryFrame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

    #make label and dropdown on potential grid sizes


        instructionLabel = Label(
            temporaryFrame,
            text='Select a size to play the game with',
            font=self.font + [24, 'bold'],
            bg = 'white',
            fg='black',
        )

        instructionLabel.place(relx=0.5, rely=0.01, relwidth=0.75, relheight=0.1, anchor='n')

        choices = list(f'{size}x{size}' for size in range(2, 11))

        setting = StringVar()
        setting.set(choices[0])

        drop = OptionMenu(self, setting, *choices)
        self.master.update()
        
        drop.place(relx=0.5, rely=0.25, relwidth=0.5, anchor='center')

        beginButton = tk2.LabelButton(
            self,
            command=lambda: (begin(temporaryFrame, setting.get()), temporaryFrame.destroy()),
            kwargs={
                'bg':'white',
                'fg': 'black',
                'font':self.font + [18],
                'text': 'Begin!!!'
            },
            clickingspeed=0.1
        )

        beginButton.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor='center')




    #save user choice

    #delete old Frame and generate matrix

    #play game


    def computer_turn(self):
        pass
    def compare_sequences(self):
        pass
    def play_game(self):
        pass
    def game_over(self):
        pass


Simon = MegaSimon(root)

root.mainloop()