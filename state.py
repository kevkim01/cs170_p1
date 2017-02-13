class State:
    def __init__(self, puzz_tiles, g_cost, h_type, h_cost, f_cost, b_index, parent):
        
        
        self.puzz_tiles = puzz_tiles            #holds the 1D array representation of the current puzzle state
        self.goal_tiles = [1,2,3,4,5,6,7,8,0]          #holds the 1D array representation of the goal state
        self.g_cost = g_cost                    #holds the cost of g(n) from initial state
        self.h_type = h_type                    #holds the heuristic type
        self.h_cost = h_cost
        self.f_cost = f_cost                    #holds the value of f(n) = g(n) + h(n)
        self.b_index = b_index                  #holds the index of the blank space
        self.parent = parent                    #holds parent state
        
    def __cmp__(self, other):
        return cmp(self.f_cost, other.f_cost)
    
    def display(self):
        print self.puzz_tiles[0],self.puzz_tiles[1],self.puzz_tiles[2]
        print self.puzz_tiles[3],self.puzz_tiles[4],self.puzz_tiles[5]
        print self.puzz_tiles[6],self.puzz_tiles[7],self.puzz_tiles[8]
        print "h_cost=", self.h_cost, " g_cost=", self.g_cost
        print "\n"
    
    
    
    def move_right(self):                       #moves the blank to the right
        x = self.b_index % 3                    #x coordinate of b_index
        y = self.b_index / 3                    #y coordinate of b index
        new_x = x + 1                           #to move right we move x to the left
        new_puzz = self.puzz_tiles[:]           #new puzzle
        
        i = new_x + (y*3)                       #new index of blank after moving
        temp = new_puzz[self.b_index]
        new_puzz[self.b_index] = new_puzz[i]
        new_puzz[i] = temp
        
        new_g_cost = self.g_cost + 1
        new_h_cost = None
        
        if(self.h_type == 1):  
             new_h_cost = 0
        if(self.h_type == 2):
            new_h_cost = Misplaced_h(new_puzz)
        if(self.h_type == 3):
            new_h_cost = Manhattan_h(new_puzz)
            
        new_f_cost = new_g_cost + new_h_cost
            
        return State(new_puzz, new_g_cost, self.h_type, new_h_cost,new_f_cost, i, self)
        
        
    def move_left(self):                        #moves the blank to the left
        x = self.b_index % 3
        y = self.b_index / 3
        new_x = x - 1
        new_puzz = self.puzz_tiles[:]
        
        i = new_x + (y*3)
        temp = new_puzz[self.b_index]
        new_puzz[self.b_index] = new_puzz[i]
        new_puzz[i] = temp
        
        new_g_cost = self.g_cost + 1
        new_h_cost = None
        
        if(self.h_type == 1):  
             new_h_cost = 0
        if(self.h_type == 2):
            new_h_cost = Misplaced_h(new_puzz)
        if(self.h_type == 3):
            new_h_cost = Manhattan_h(new_puzz)
            
        new_f_cost = new_g_cost + new_h_cost
            
        return State(new_puzz, new_g_cost, self.h_type, new_h_cost,new_f_cost, i, self)
        
        
    def move_down(self):                        #moves the blank down
        x = self.b_index % 3
        y = self.b_index / 3
        new_y = y + 1
        new_puzz = self.puzz_tiles[:]
        
        i = x + (new_y*3)
        temp = new_puzz[self.b_index]
        new_puzz[self.b_index] = new_puzz[i]
        new_puzz[i] = temp
        
        new_g_cost = self.g_cost + 1
        new_h_cost = None
        
        if(self.h_type == 1):  
             new_h_cost = 0
        if(self.h_type == 2):
            new_h_cost = Misplaced_h(new_puzz)
        if(self.h_type == 3):
            new_h_cost = Manhattan_h(new_puzz)
            
        new_f_cost = new_g_cost + new_h_cost
            
        return State(new_puzz, new_g_cost, self.h_type, new_h_cost,new_f_cost, i, self)
        
    def move_up(self):                          #moves the blank up
        x = self.b_index % 3
        y = self.b_index / 3
        new_y = y - 1
        new_puzz = self.puzz_tiles[:]
        
        i = x + (new_y*3)
        temp = new_puzz[self.b_index]
        new_puzz[self.b_index] = new_puzz[i]
        new_puzz[i] = temp
        
        new_g_cost = self.g_cost + 1
        new_h_cost = None
        
        if(self.h_type == 1):  
             new_h_cost = 0
        if(self.h_type == 2):
            new_h_cost = Misplaced_h(new_puzz)
        if(self.h_type == 3):
            new_h_cost = Manhattan_h(new_puzz)
            
        new_f_cost = new_g_cost + new_h_cost
            
        return State(new_puzz, new_g_cost, self.h_type, new_h_cost,new_f_cost, i, self)   
        
        
    def check_move(self):                           #function used to see where blank can move
        x = self.b_index % 3
        y = self.b_index / 3
        next_states = []
        
        """
        this portion of the code will check where the blank is and see where it can move
        it will create new states based on where the blank can move and store them in a 
        list, the list will be returned so that it can be pushed onto the queue
        """
        if(x == 0):                                         #if the blank is at x-coord 0
            if(y == 0):
                next_states.append(self.move_right())
                next_states.append(self.move_down())
                
                
            elif(y == 1):
                next_states.append(self.move_up())
                next_states.append(self.move_down())
                next_states.append(self.move_right())
                
            elif(y ==2):
                next_states.append(self.move_up())
                next_states.append(self.move_right())
        
        elif(x == 1):                                       #if the blank is at x-coord 1
            if(y == 0):
                next_states.append(self.move_down())
                next_states.append(self.move_left())
                next_states.append(self.move_right())
                
            elif(y == 1):
                next_states.append(self.move_up())
                next_states.append(self.move_down())
                next_states.append(self.move_right())
                next_states.append(self.move_left())
                
            elif(y ==2):
                next_states.append(self.move_up())
                next_states.append(self.move_left())
                next_states.append(self.move_right())
        
        elif(x == 2):                                       #if the blank is at x-coord 2
            if(y == 0):
                next_states.append(self.move_down())
                next_states.append(self.move_left())
                
            elif(y == 1):
                next_states.append(self.move_up())
                next_states.append(self.move_down())
                next_states.append(self.move_left())
                
            elif(y ==2):
                next_states.append(self.move_up())
                next_states.append(self.move_left())
        return next_states

    
    def trace_path(self, init_state, nodes_expanded, nodes_queue):      #this function will trace the path back from the goal node
        trace = []
        trace.append(self)
        i = self.parent
        
        print "Expanding State"
        init_state.display()
        
        while i.puzz_tiles != init_state.puzz_tiles :
            trace.append(i)
            i = i.parent
        
        for i in reversed(range(len(trace))):                           #this will print out the path in order
            trace[i].display()
            
        print "the search algorithm expanded a total of", nodes_expanded, "nodes."
        print "the maximum number of nodes in the queue at any one time was", nodes_queue
        print "the depth of the goal node was", self.g_cost

def Manhattan_h(puzzle):                      #calculates the h(n) for manhattan dist
    h = 0
    width = 3
    goal_tiles = [1,2,3,4,5,6,7,8,0]
    for i in puzzle:
        if(i == 0):
            continue
        x = puzzle.index(i)
        y = goal_tiles.index(i)
        
        if(x != y):
            h += abs((x % width) - (y % width)) + abs((x / width) - (y / width))
    return h


def Misplaced_h(puzzle):                      #calculates h(n) for misplaced tile
    h = 0
    goal_tiles = [1,2,3,4,5,6,7,8,0]
    for i in range(len(puzzle)):
        if(puzzle[i] == 0):
            continue
        if puzzle[i] != goal_tiles[i]:
            h += 1
    return h    

