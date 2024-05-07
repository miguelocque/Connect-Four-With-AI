#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111 - Miguel Ocque - mocque@bu.edu (worked alone)
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        """ constructor for the Board class """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        
        # adds the hyphens
        for i in range((self.width * 2) + 1):
            s += '-'
            
        s += '\n'
        
        # adds the column indices
        for i in range(self.width):
            s += ' '
            
            i = str(i % 10)
            
            s +=  i 
            
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0
        while self.slots[row][col] == ' ':
           if row == self.height - 1:
               break
           elif self.slots[row + 1][col] != ' ':
               break
           else:
               row += 1
           
            
        self.slots[row][col] = checker
    
    ### add your reset method here ###
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    
    
    # resetting the board method:
        
    def reset(self):
        """ resets the board by assigning all slots to contain 
            a space character. uses list comprehension
        """
        
        self.slots = [[' '] * self.width for row in range(self.height)]


    # can add more to the board method:
    
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the
            column col on the calling Board object. Otherwise, it 
            should return False. The method should make sure that
            col is in the range from 0 to the last column on the 
            board and that the specified column is not full.
        """
        if col < 0 or col >= self.width:
            return False
        
        for i in range(self.height):
            if self.slots[i][col] == ' ':
                return True
            
        return False
    
    # method to check if the board is full:
        
    def is_full(self):
        """ returns True if the called Board object is completely 
            full of checkers, and returns False otherwise. Utilizes
            the 'can_add_to' method written above
        """
        
        for row in range(self.height):
            for col in range(self.width):
                if self.can_add_to(col) == True:
                    return False
                      
        return True
        
            
    # method for removing the top checker of the given col:
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called 
            Board object. If the column is empty, then the method
            should do nothing.
        """
        
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
                
            
    # method for checking a win for either player:
        
    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 'O',
            and returns True if there are four consecutive slots 
            containing checker on the board. Otherwise, it should 
            return False.
                a win in Connect Four occurs when there are four 
                consecutive checkers of the same type either 
                horizontally, vertically, or diagonally. Moreoever, 
                there are two diagonal orientations: going “up” from 
                left to right, and going “down” from left to right.
        """
        assert(checker == 'X' or checker == 'O')
        
        winner = False
        
        winner = self.is_horizontal_win(checker)
        if winner == True:
            return winner
        winner = self.is_vertical_win(checker)
        if winner == True:
            return winner
        winner = self.is_down_diagonal_win(checker)
        if winner == True:
            return winner
        winner = self.is_up_diagonal_win(checker)
        if winner == True:
            return winner
        
        return winner
            
        
    # helper functions below for the is_win_for method:
        
    # checks a horizontal win
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                            self.slots[row][col + 3] == checker:
                                return True

        # if we make it here, there were no horizontal wins
        return False
        
    
    # checks a vertical win
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker
        """
        
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                            self.slots[row + 3][col] == checker:
                                return True

        # if we make it here, there were no horizontal wins
        return False
        
        
    # checks a diagonal up win
    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal down win for the specified checker
        """
        
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                        self.slots[row + 2][col + 2] == checker and \
                            self.slots[row + 3][col + 3] == checker:
                                return True
                                        
        return False
        
        
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal up win for the specified checker
        """
        
        r = range(self.height)
        r = r[:(self.height - 3):-1]
        
        for row in r:
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                        self.slots[row - 2][col + 2] == checker and \
                            self.slots[row - 3][col + 3] == checker:
                                return True
                            
        return False
                            
                            
        
    
    
    
    
    
    