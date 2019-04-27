# Maximize the score #
# 2801ICT Project 2 - s5131071 - Rusty Blewitt #

import sys  # Get command line args
import os   # Get cwd


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
    line_one = f.readline().split()         # Input 1/3

    ball_count = line_one[0]
    turn_count = line_one[1]

    balls = f.readline()                    # Input 2/3
    toss = f.readline()                     # Input 3/3
    
    # scotts_heap
    # rustys_heap
