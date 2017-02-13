import math
import Queue as Q
import state
import problem
    

print "Welcome to 861168574's 8-puzzle solver."
print "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle."
uinput1 = input()

init_state = None                                   #will hold the inital state of 

puzzle = None                                       #holds 1D repr. of puzzle
g_cost = 0                                          #g(n) = 0 initially
h_type = None
h_cost = None
b_index = None
par = None


if(uinput1 == 1):
    puzzle = [1,2,3,4,8,0,7,6,5]                    #default (for testing)
    b_index = puzzle.index(0)                       #recieves the index of the blank 
    

elif(uinput1 == 2):
    print "Enter your puzzle, use a zero to represent the blank"
    row1 = [int(i) for i in raw_input("Enter the 1st row, use space between numbers: ").split()]
    row2 = [int(i) for i in raw_input("Enter the 1st row, use space between numbers: ").split()]
    row3 = [int(i) for i in raw_input("Enter the 1st row, use space between numbers: ").split()]
    
    puzzle = row1+row2+row3                         #combine all the rows into a 1D array
    b_index = puzzle.index(0)                       #recieves the index of the blank 
    
    
print "Enter your choice of algorithm"
print "\t 1. Uniform Cost Search"
print "\t 2. A* with misplaced tile heuristic"
print "\t 3. A* with Manhattan distance heuristic"

h_type = input()


if(h_type == 1):                                    #if the problem is ucs h(n) = 0
    h_cost = 0
    
if(h_type == 2):                                    #if the problem is misplaced a*
    h_cost = state.Misplaced_h(puzzle)
    
if(h_type ==3):
    h_cost = state.Manhattan_h(puzzle)              #if the problem is manhattan a*

f_cost = g_cost + h_cost
init_state = state.State(puzzle, g_cost, h_type, h_cost, g_cost, b_index, 0)    #initial state of problem created

problem = problem.Problem(init_state)               #create instance of the entire problem

problem.Solve()                                     #solve the puzzle
