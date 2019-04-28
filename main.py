# Maximize the score #
# 2801ICT Project 2 - s5131071 - Rusty Blewitt #

import sys  # Get command line args
import os   # Get cwd
from priority_q import scott_q, rusty_q


# Opening of input file ------------
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
#-----------------------------------


T = int(f.readline())                   # Number of test cases
print("Test cases: ", T)

for t in range(T):                      # For each test case...
    # print("\n\n")
    scotts_q = scott_q()                            # Init priority queues
    rustys_q = rusty_q()

    line_one = f.readline().split()                 # Input 1/3 : Amount of balls, and turns allowed each round
    ball_count = int(line_one[0])
    turn_count = int(line_one[1])

    balls = [int(b) for b in f.readline().split()]  # Input 2/3 : Available balls
    for b in balls:
        scotts_q.enqueue(int(b))
        rustys_q.enqueue(int(b))

    toss = f.readline()                             # Input 3/3 : Result of the toin coss
    scotts_turn = 'HEADS' in toss

    scotts_score = 0                                # Init scores
    rustys_score = 0
    

    for turn in range(ball_count):                  
        # print(turn)
        if (turn % turn_count == 0 and turn > 0):
            scotts_turn = not scotts_turn
        
        if scotts_turn:     # Scotts turn
            pick = scotts_q.dequeue()
            while(pick not in balls):               # Pick again if ball already used
                pick = scotts_q.dequeue()
            balls.remove(pick)
            scotts_score += pick
            # print("Scotts turn. Picked %d. Score now %d" %(pick, scotts_score))
        
        else:               # Rustys turn
            pick = rustys_q.dequeue()
            while(pick not in balls):              # Pick again if ball already used
                pick = rustys_q.dequeue()
            balls.remove(pick)
            rustys_score += pick 
            # print("Rustys turn. Picked %d. Score now %d" %(pick, rustys_score))
    
    print("%d %d" %(scotts_score, rustys_score))
