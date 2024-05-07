#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  
# CS111 - Miguel Ocque - mocque@bu.edu (worked alone)
#

from ps9pr1 import Board

# write your class below.

class Player():
    """ a data type for a connect four game that holds attributes
        for a player
    """
    
    # initializing the contstructor:
    def __init__(self, checker):
        """ initializes the Player object, assigning it a 
            checker that is either 'X' or 'O.' It also contains
            a variable 'num_moves' which determines how many moves 
            the player has done.
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    # initializing the repr method:
    def __repr__(self):
        """ returns a string representing a Player object. The 
            string returned should indicate which checker the 
            Player object is using
        """
        s = 'Player '
        s += self.checker
        
        return s
    
    # opponent checker method:
    def opponent_checker(self):
        """ returns a one-character string representing the checker
            of the Player object’s opponent. The method may assume 
            that the calling Player object has a checker attribute 
            that is either 'X' or 'O'
        """
        
        opp = ''
        if self.checker == 'X':
            opp = 'O'
            
        else:
            opp = 'X'
            
        return opp
    
    # next move method:
    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns the 
            column where the player wants to make the next move. To do 
            this, the method should ask the user to enter a column number 
            that represents where the user wants to place a checker on the 
            board. The method should repeatedly ask for a column number 
            until a valid column number is given. Additionally, this method
            should increment the number of moves that the Player object has 
            made.
        """
        
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            
            if col >= 0 and col < b.width:
                if b.can_add_to(col) == True:
                    return col
            
            elif col < 0 or col >= b.width: 
                print('Try again!')
            
        
    
    
    
    
    
    
    
    