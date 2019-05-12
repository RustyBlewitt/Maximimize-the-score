# Problem
 Two players, Scott and Rusty are to attempt to win a game each using their own strategy. The game involves each player taking turns at picking a certain amount of numbered balls from a given set in an effort to maximize their score. Scott will always take the highest value ball where Rusty will get the sum of digits of that ball. For example: a ball with ​914​ on it. Rusty will see this ball as ​9+1+4​ = ​15.​ Where Scott sees the ball as it’s real value, 914.

 In both cases, the real number on the ball is what that ball’s value is. In the above example, although Rusty considers this ball of value 15, if Rusty does pick this ball up, he receives the full 914 score associated with it.

 The amount of balls that can be picked up at a time is pre-decided and a pre-decided coin toss determines who gets to take the first ball.
# Inputs and outputs
 The program will initially take one input as an argument to be passed when the program is run, this should be the path of the input file.
 The input file should consist of one leading line, which has a single number n, followed by n * 3 lines of additional inputs.
 N represents how many games this file will provide input for. The 3 lines for each n (for each game) provide the following information.<br/>
 &nbsp;&nbsp;&nbsp;&nbsp;Line 1: Integers x & y.<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X = Total number of balls available<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Y = Amount of balls that can be picked in one turn<br/>
 &nbsp;&nbsp;&nbsp;&nbsp;Line 2: The available balls to select.<br/>
 &nbsp;&nbsp;&nbsp;&nbsp;Line 3: The result of the coin toss, deciding who gets the first turn.<br/>

# Algorithm description
 The algorithm used can best be described as a greedy approach using heap data structures as priority queues.
 Each player, Scott and Rusty, are greedy in that at any given time they’re only factoring in the best possible choice at that moment.
 The balls for each game are represented as objects of the class Ball. Each player then creates a reference to that ball object and each player’s priority queue (their own order of priority in which they plan to best pick their balls) is filled with these references.
 Each ball object stores three pieces of information specific to that ball:
     1. Used (True/False). This is simply an indication as to whether the ball has been previously selected, in which case the player will discard that reference then try the next item in their priority queue.
     2. Real_val (Integer number). This number represents the true value of that ball. Which is, regardless of either player’s interpretation, the value that will be added to the score of the player who picks the ball up.
     3. Digit_val (Integer number). This number represent the sum of digits of the ball. Further clarification: Real_val = 123, Digit_val = (1+2+3) = 6.

 Additionally to these three variables, the Ball class has a digit_val method, which upon object initialisation calculates and stores the digit sum value of the real value.
 The player’s priority queues are populated one ball at a time, using the common heapify up approach. Heapify up involves inserting the ball in the last available position of the priority queue then from that position the ball finds its way up the binary tree, trading places with each parent node that it has higher priority then.
 Using this approach, you maintain the requirement of each parent being of greater priority than it’s children.
 A problem specific variation to this is that, where in general one would simply only trade places with a parent if the child was explicitly greater value than it, in Rusty’s queue he must check for equality between parent and child and if they are equal he must then use the real value of the two balls to break the tie in hopes of maximising his score.

 The result of the coin toss is noted and a reference to the winning players’ queue object is stored as player. Then, once for each ball that’s initially available, the program loops allowing the current player to grab a ball reference from their priority queue until they find one that refers to an unused ball, at which point they will add the value of that ball to their score, set the ball object to ​used​ and end their while loop. Alternatively the while loop will terminate when a players heap is empty however this is just a fail-safe to prevent dequeuing from an empty queue and if correct inputs are given this case shouldn’t ever occur.
 For each ball that’s picked, if that is the n-th ball, and n % (amount of balls players can pick at a time) == 0, then the player reference is switched to the other player.
 The game is over when all balls have been picked and each players score is printed to standard output.
