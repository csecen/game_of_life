import numpy as np
import matplotlib.pyplot as plt

class Game_Of_Life():
    '''
    The game of life is a game created by John Conway to illustrate that simple
    rules can be used to create complex systems. The rules for the game are:
        1) Any live cell with fewer than two live neighbours dies, as if by 
           underpopulation.
        2) Any live cell with two or three live neighbours lives on to the next
           generation.
        3) Any live cell with more than three live neighbours dies, as if by
           overpopulation.
        4) Any dead cell with exactly three live neighbours becomes a live
           cell, as if by reproduction.
    By using this program you will be able to see the complexity that these
    rules create and experiment with how different board initialization can
    effect the end result.
    '''
    
    def __init__(self, size):
        '''
        Creates an instance of the game and makes a new square board that is 
        randomly initialized.
        
        Input:
            size --> integer indicating the size of the board, both height and
                     width.
        '''
#         self.board = np.zeros((size,size))
        self.board = np.random.randint(low=0, high=2, size=(size, size))
        self.size = size
    
    
    def define_board(self, board):
        '''
        Allows the user to define their own board. This will reset the original
        board.
        
        Input:
            board --> square 2d numpy array that represents the new board.
        '''
        try:
            x, y = board.shape
            if x != y:
                print('Oh no. The board must be square.')
            else:
                self.board = board
            
        except AttributeError:
            print('Oh no. The board must be a numpy array.')
            
    
    def step(self):
        '''
        Performs a single step of the game using the following rules defined
        for the game of life:
            1) Any live cell with fewer than two live neighbours dies, as if by 
               underpopulation.
            2) Any live cell with two or three live neighbours lives on to the next
               generation.
            3) Any live cell with more than three live neighbours dies, as if by
               overpopulation.
            4) Any dead cell with exactly three live neighbours becomes a live
               cell, as if by reproduction.
        '''
        temp_board = np.copy(self.board)
        
        for row in range(self.size):
            for col in range(self.size):
                sum = 0
                curr = temp_board[row][col]
                
                index_array = [(row-1, col-1), (row-1, col-0), (row-1, col+1), 
                               (row-0, col-1), (row-0, col+1), (row+1, col-1), 
                               (row+1, col+0), (row+1, col+1)]
                    
                for idx_row, idx_col in index_array:
                    if idx_row < 0 or idx_col < 0 or idx_row >= self.size or idx_col >= self.size :
                        pass
                    else:
                        sum += temp_board[idx_row][idx_col]
                
                if curr == 0:
                    if sum == 3:
                        self.board[row][col] = 1
                else:
                    if (sum < 2) or (sum > 3):
                        self.board[row][col] = 0
            
    
    def run(self, steps):
        '''
        Runs the game for the specified number of steps given by the user.
        
        Input:
            steps --> number of steps of the game to be made.
        '''
        for _ in range(steps):
            self.step()
            self.view_board()
    
    
    def view_board(self):
        '''
        Displays the board in it's current state.
        '''
        plt.imshow(self.board, cmap='binary')
        plt.show