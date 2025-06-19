from matrix import *
import sys

sys.path.append('/Users/anayaahanotu/Documents/Coding/GitHub/Special_tkinter_objects/')

import tkinterPlus2 as tk2


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

        self.score = 0
        self.highscore = 0

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

        self.master.update()

        self.computer_sequence = []
        self.player_sequence = []

        self.playerTurn = False
        self.playerWinning = None
        self.size = 2

        self.setup()




    def setup(self):

    #create temporary Frame

    #make function to set up matrix

        self.title.configure(
            text='Simon!!'
        )

        def begin(size, oldFrame):

            oldFrame.destroy()

            self.master.update()

            size = list(item for item in size if item.isnumeric())
            size = size[:len(size)//2]

            matrixSize = ''

            for element in size: matrixSize += element

            matrixSize = int(matrixSize)
            self.size = matrixSize

            self.matrix = Square_Matrix(self, matrixSize)
            self.matrix.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)
            self.matrix.bind_all('<Button>', lambda e: self.compare_sequences(), '+')

            self.master.update()

            self.computer_sequence = []
            self.player_sequence = []

            self.playerTurn = False
            self.playerWinning = True

            self.play_game()

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

        choices = list(f'{size}x{size}' for size in range(2, 16))

        setting = StringVar()
        setting.set(choices[0])

        drop = OptionMenu(temporaryFrame, setting, *choices)
        self.master.update()
        
        drop.place(relx=0.5, rely=0.25, relwidth=0.5, anchor='center')

        beginButton = tk2.LabelButton(
            temporaryFrame,
            command=lambda: (begin(setting.get(), temporaryFrame)),
            kwargs={
                'bg':'white',
                'fg': 'black',
                'font':self.font + [18],
                'text': 'Begin!!!'
            },
            clickingspeed=0.1
        )

        beginButton.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor='center')
        self.master.update()

    def computer_turn(self):
        '''
        computer_turn
        has the computer take their turn
        '''


        self.title.configure(
            text='Computer Turn',
            font=self.font + ['40']
        )

        root.update()
        time.sleep(1)

        for location in self.computer_sequence:
            self.matrix.button_pressed(location)
            time.sleep(1)
        
        self.computer_sequence.append(
            (random.randrange(self.size), random.randrange(self.size))
        )

        self.matrix.button_pressed(self.computer_sequence[-1])
        self.master.update()

        

    def compare_sequences(self):
        '''
        compare_sequences()
        make sure the user did not make any mistakes
        '''


        if self.playerTurn:
            self.player_sequence.append(self.matrix.lastButton)

            if self.computer_sequence[:len(self.player_sequence)] != self.player_sequence: 
                self.playerWinning = False

    def play_game(self):
        '''
        play_game()
        plays a game of mega simon
        '''
        while self.playerWinning:
            if len(self.player_sequence) == len(self.computer_sequence):
                self.playerTurn = False
                self.score = len(self.player_sequence)
                if self.highscore < self.score: 
                    self.highscore = self.score

                self.highScoreLabel['text'] = f'High score: {self.highscore}'
                self.scoreLabel['text'] = f'Score: {self.score}'
                self.master.update()

                self.player_sequence = []
                self.computer_turn()
                self.master.update()
            else:
                self.playerTurn = True
                self.master.update()


                self.title.configure(
                    text='Your turn',
                )

                self.master.update()

        self.game_over()
        self.player_sequence = []

    def game_over(self):
        '''
        make game_over frame
        '''

        self.matrix.unbind_all(['<Button>'])
        self.matrix.destroy()
        

        self.master.update()
        self.title.configure(
            text='GAME OVER'
        )
    
        temporaryFrame = Frame(
            self,
            bg=self['bg']
        )
        temporaryFrame.pack(fill='both', expand=1)

        instructionLabel = Label(
            temporaryFrame,
            text='Play again or quit the game?',
            bg='white',
            fg='black',
            font=self.font + [20]
        )
        instructionLabel.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1, anchor='n')

        restartButton = tk2.LabelButton(
            temporaryFrame,
            command= lambda: (self.setup(), temporaryFrame.destroy()),
            kwargs={
                'bg': 'white',
                'fg': 'black',
                'text': 'Play again',
                'font': self.font + [18]
            }
        )

        restartButton.place(relx=0.25, rely=0.25, relwidth=0.25, relheight=0.1, anchor='center')

        endButton = tk2.LabelButton(
            temporaryFrame,
            command= lambda: (root.destroy()),
            kwargs={
                'bg': 'white',
                'fg': 'black',
                'text': 'end game',
                'font': self.font + [18]
            }
        )

        endButton.place(relx=0.75, rely=0.25, relwidth=0.25, relheight=0.1, anchor='center')
        

Simon = MegaSimon(root)

root.mainloop()