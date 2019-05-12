# Rusty Blewitt | Maximise the Score

import sys  # Get command line args
import os   # Get cwd

# -------------------- Program class declarations start here ------------------------
class Ball:
    def __init__(self, val):
        self.used = False       # Track if this ball has been used by either party
        self.real_val = val     # Store real value of this ball
        self.digit_val(val)     # Call digit_val() get and store digit value of this ball

    def digit_val(self, n):     # Calculates the sum of the digits in a number
        self.digit_val = 0
        while(n > 0):
            self.digit_val += n % 10
            n = n // 10
        

class PriorityQ:
    def __init__(self):
        self.nodes = []         # Init nodes list
        self.score = 0          # Keep track of game score that this queue produces

    def get_parent(self, child):        #   
        return (child - 1) // 2         #
                                        #
    def get_left_child(self, parent):   # Helper methods to get useful
        return (parent * 2) + 1         # indexes of items in heap
                                        #
    def get_right_child(self, parent):  #
        return (parent * 2) + 2         #

    def heapify_up(self):
        child = len(self.nodes) - 1                     # Child = right-most leaf node (where recent insertion will be)
        parent = self.get_parent(len(self.nodes) - 1)   # Use helper method to get parent of child

        while(self.nodes[child].real_val > self.nodes[parent].real_val):
            temp = self.nodes[parent]               #
            self.nodes[parent] = self.nodes[child]  # Switch child and parent 
            self.nodes[child] = temp                #

            child = parent                          # Move up the tree, make old parent new child
            if child == 0:                          # If old parent (new child) is root..
                break                                   # .. break
            parent = self.get_parent(child)         # Otherwise get new parent and repeat

    def heapify_down(self):
        parent = 0                              # Parent = root node
        left_child = self.get_left_child(0)     # Use helper methods to get parent's children
        right_child = self.get_right_child(0)   #

        while(1):
            if left_child >= len(self.nodes):       # If parent is leaf node..
                break                                 # .. break

            elif right_child >= len(self.nodes):    # If parent only has left child ..
                max_child = left_child                # .. make this max child

            else:                                   # If parent has two children ...
                # If left child has greater real value than right child ...
                if self.nodes[left_child].real_val > self.nodes[right_child].real_val:
                    # ... left child is max child
                    max_child = left_child
                # If right child has greater real value than left child ...
                else:
                    # ... right child is max child
                    max_child = right_child

            # If max child has greater real value than parent...
            if self.nodes[max_child].real_val > self.nodes[parent].real_val:
                temp = self.nodes[parent]                   #
                self.nodes[parent] = self.nodes[max_child]  # Switch parent and max child
                self.nodes[max_child] = temp                #

                parent = max_child                          # Move down the tree, make old child new parent
                left_child = self.get_left_child(parent)    # Use helper methods to get new parent's children
                right_child = self.get_right_child(parent)  #

            # Break if parent and max child in correct order
            else:
                break

    def enqueue(self, n):
        self.nodes.append(n)             # Add enqueued node to end of list
        if len(self.nodes) > 1:          # If enqueued node was not first in list ..
            self.heapify_up()                # .. perform heapify up

    def dequeue(self):
        if len(self.nodes) == 1:         #
            return self.nodes.pop()      #
                                         # If only one or two nodes, simply return only / first priority node
        if len(self.nodes) == 2:         #
            return self.nodes.pop(0)     #

        root = self.nodes[0]             # Mark the root node

        self.nodes[0] = self.nodes.pop() # Pop from end of list and place at front (root)
        self.heapify_down()              # Heapify down from root to recorrect order

        return root


# Inherits from regular priority queue
class DigitValuePriorityQ(PriorityQ):

    # Override method to prioritise digit values
    def heapify_up(self): 
        child = len(self.nodes) - 1                     # Child = right-most leaf node (where recent insertion will be)
        parent = self.get_parent(len(self.nodes) - 1)   # Use inherited method to get parent of this child

        while(self.nodes[child].digit_val >= self.nodes[parent].digit_val): # While child > parent    
            if(self.nodes[child].digit_val == self.nodes[parent].digit_val):    #   If even...
                if(self.nodes[child].real_val < self.nodes[parent].real_val):     #   ... and real val order in place...
                    break                                                           #   ... this is correct order, break.
            temp = self.nodes[parent]                       #
            self.nodes[parent] = self.nodes[child]          # Switch parent and child
            self.nodes[child] = temp                        #

            child = parent                                  # Move up the tree, make old parent new child
            if child == 0:                                  # If old parent (new child) is root...
                break                                           # ... break
            parent = self.get_parent(child)                 # Otherwise get new parent and repeat

    # Override method to prioritise digit values
    def heapify_down(self):                 
        parent = 0                              # Parent = root node
        left_child = self.get_left_child(0)     # Use inherited methods to get children
        right_child = self.get_right_child(0)   # #

        while(1):
            if left_child >= len(self.nodes):   # If parent is leaf node...
                break                               # ... break

            elif right_child >= len(self.nodes):  # If parent only has left child...
                max_child = left_child              # ... make this max child

            
            else:                               # If parent has two children...
                # If left child has greater digit value than right child
                if self.nodes[left_child].digit_val > self.nodes[right_child].digit_val:
                    max_child = left_child

                # If children have equivalent digit values...
                elif self.nodes[left_child].digit_val == self.nodes[right_child].digit_val:

                    # ...and the left child has a greater real value
                    if self.nodes[left_child].real_val > self.nodes[right_child].real_val:
                        max_child = left_child
                    # ...and the right child has a greater real value
                    else:
                        max_child = right_child
                # If right child has greater digit value than left child
                else:
                    max_child = right_child

            # If max child digit value greater or equal to parent digit value...
            if self.nodes[max_child].digit_val >= self.nodes[parent].digit_val:

                # If max child has EQUAL digit value to parent, then check real value...
                if self.nodes[max_child].digit_val == self.nodes[parent].digit_val:
                    # If real value in correct order (parent > child), break here.
                    if self.nodes[parent].real_val > self.nodes[max_child].real_val:
                        break

                temp = self.nodes[parent]                   #
                self.nodes[parent] = self.nodes[max_child]  # Switch parent and child
                self.nodes[max_child] = temp                #

                parent = max_child                          # Move down tree, make old child new parent
                left_child = self.get_left_child(parent)    # Use inherited methods to get left and ..
                right_child = self.get_right_child(parent)  # .. right children of new parent

            else:
                break

# -------------------- Program class declarations end here ------------------------


# ------------------------- Main program starts here ------------------------------

# Opening of input file ----
try:
    fname = sys.argv[1]
except IndexError:
    print("\nNo input file given. Try to run program again passing your input file as the only argument.")
    print("For example: main.py test_input.txt\n")
    exit(1)

try:
    f = open(fname)
except FileNotFoundError :
    print("\nThe file '%s' could not be opened, please check filename and path " %fname +
            "relative to %s then try again.\n" %os.getcwd())
    exit(1)
#----------------------------


T = int(f.readline())                   # Number of Test cases

for t in range(T):                      # For each test case...

    scotts_q = PriorityQ()                 # Init priority queues
    rustys_q = DigitValuePriorityQ()       #

    line_one = f.readline().split()     # Input 1/3 : Amount of balls, and turns allowed each round
    ball_count = int(line_one[0])   
    turn_count = int(line_one[1])

    for n in f.readline().split():      # Input 2/3 : Available balls
        b = Ball(int(n))                    # Init ball object
        scotts_q.enqueue(b)                 # Pass a reference of that object to Scott's queue
        rustys_q.enqueue(b)                 # Pass a reference of that object to Rusty's queue

    toss = f.readline()                 # Input 3/3 : Result of the coin toss

    # Current player is Rusty if coin toss is tails, otherwise Scott
    player = rustys_q if 'TAILS' in toss else scotts_q

    for turn in range(1, ball_count+1): # For each turn (each unique ball)
        while( len(player.nodes) > 0 ):     # While player still has ball references in their queue
            pick = player.dequeue()             # Pick highest priority ball for that player

            if not pick.used:                   # If ball picked hasn't yet been picked
                player.score += pick.real_val   # Player adds that balls value to their score
                pick.used = True                # Ball object is marked as having been picked
                break

        if (turn % turn_count == 0):        # If next player's turn next, switch current player
            player = scotts_q if player == rustys_q else rustys_q


    print("%d %d" %(scotts_q.score, rustys_q.score))

# ------------------------- Main program ends here ------------------------------