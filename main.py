import sys  # Get command line args
import os   # Get cwd
from ball_and_queues import Ball, PriorityQ, DigitValuePriorityQ

# Opening of input file ----
try:
    fname = sys.argv[1]
except IndexError:
    print("No input file given. Try to run program again passing your input file as the only argument")
    exit(1)

try:
    f = open(fname)
except FileNotFoundError :
    print("The file '%s' could not be opened, please check filename and path " %fname +
            "relative to %s then try again." %os.getcwd())
    exit(1)
#----------------------------

T = int(f.readline())                   # Number of test cases

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

    toss = f.readline()                 # Input 3/3 : Result of the toin coss

    # Current player is Rusty if toin coss is tails, otherwise Scott
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