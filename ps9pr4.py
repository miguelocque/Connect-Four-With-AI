#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#
# CS111 - Miguel Ocque - mocque@bu.edu (worked alone)
#

import random  
from ps9pr3 import *


class AIPlayer(Player):
    """ a class that createas an intelligent AI Player that 
        is a subclass of the Player class.
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ overrides the constructor inherited from the Player class
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)    
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        """ overrides the repr method inherited from the Player class
            indicates the checker, tiebreaking strategy, and lookahead
        """
        
        s = 'Player '
        
        # adds the checker to the string
        s += self.checker
        
        # adds the tiebreaking strategy and the lookahead to the string
        s += ' ('
        s += self.tiebreak
        s += ', '
        s += str(self.lookahead)
        s += ')'
        
        return s
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column 
            of the board, and that returns the index of the column 
            with the maximum score. If one or more columns are tied
            for the maximum score, the method should apply the called 
            AIPlayer‘s tiebreaking strategy to break the tie. Returns
            the index of the appropriate column, not the column’s score.
        """
        
        max = scores[0]
        
        # looping through the list scores to determine the highest score
        for i in range(len(scores)):
            if scores[i] > max:
                max = scores[i]
                
        
        # now looping through again and creating a new list at which 
        # the max score occurs
        
        inst = []
        for i in range(len(scores)):
            if scores[i] == max:
                inst += [i]
                
        
        # using the tiebreaking strategy, we determine what to return
        if self.tiebreak == 'LEFT':
            return inst[0]
        elif self.tiebreak == 'RIGHT':
            return inst[-1]
        else:
            return random.choice(inst)

    

    def scores_for(self, b):
        """ Takes a Board object b and determines the called AIPlayer‘s 
            scores for the columns in b. Each column should be assigned 
            one of the four possible scores discussed in the Overview 
            at the start of this problem, based on the called AIPlayer‘s
            lookahead value. The method should return a list containing
            one score for each column.
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                
                # determining whether to change a score to 0 or 100
                
                # if the opponent's max score is 0, score is 100 because 
                # we have a win.
                if max(opp_scores) == 0:
                    scores[col] = 100
                # elif the opponent's max score is 100, score is 0 at the
                # col because the opponent has reached a win.
                elif max(opp_scores) == 100:
                    scores[col] = 0
                
                # 50s should be taken care of at this point
                    
                b.remove_checker(col)
                
        return scores
    
            
                    
    def next_move(self, b):
        """ the next_move method that is inherited from Player. Rather 
            than asking the user for the next move, this version of 
            next_move should return the called AIPlayer‘s judgment of 
            its best possible move. Utilizes the max_score_column and
            scores_for methods written above.
        """
        
        # getting the list of best scores and the col index for the next move
        lst = self.scores_for(b)
        nxt_move = self.max_score_column(lst)
        
        # increments the number of moves
        self.num_moves += 1
        
        return nxt_move
                
        
        
        
        
        
        
        