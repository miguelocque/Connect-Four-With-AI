#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#
# CS111 - Miguel Ocque - mocque@bu.edu (worked alone)
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b


# Task 1:
def process_move(p, b):
    """ Takes two parameters: a Player object p for the player whose 
        move is being processed, and a Board object b for the board 
        on which the game is being played. will perform all of the 
        steps involved in processing a single move by player p on 
        board b.
        Does:
            1. Print a message that specifies whose turn it is
            2. Obtain player p‘s next move by using p to call 
               the appropriate Player method. Store the move 
               (i.e., the selected column number) in an appropriately 
               named variable.
            3. Apply the move to the board by using b to call the 
               appropriate Board method.
            4. Print a blank line, and then print board b.
            5. Check to see if the move resulted in a win or a tie
               by using the appropriate methods in b.
            6. If it is neither a win nor a tie, the method should 
               simply return False.
    """
    
    # takes care of 1.
    print(p)
    
    # takes care of 2. 
    p_next = p.next_move(b)
    
    # takes care of 3.
    b.add_checker(p.checker, p_next)
    
    # takes care of 4. 
    print('\n')
    print(b)
    
    # takes care of 5 and 6.
    result = b.is_win_for(p.checker)
    if result == True:
        print(p, 'wins in' , str(p.num_moves), 'moves!')
        print('Congratulations!')
        return result
        
    elif b.is_full() == True:
        print("It's a Tie!")
        return True
    
    else:
        return False
    
class RandomPlayer(Player):
    """ a new class that creates an unintelligent AI. This is a 
        subclass of the Player class, thus inherits all its 
        methods.
    """
    
    def next_move(self, b):
        """ overrides (i.e., replaces) the next_move method that
            is inherited from Player. Rather than asking the user 
            for the next move, this version of next_move should 
            choose at random from the columns in the board b that 
            are not yet full, and return the index of that randomly
            selected column. You may assume that this method will 
            only be called in cases in which there is at least one 
            available column.
        """
        
        pos_cols = [x for x in range(b.width) if b.can_add_to(x) == True]
        
        self.num_moves += 1
        
        return random.choice(pos_cols)
    
    
    
    
    
    
    