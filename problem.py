import math
import Queue as Q
import state

class P_queue():
    def __init__(self):
        arr = []
    


class Problem():
    def __init__(self, init_state):
        self.init_state = init_state                                    #State object
        self.goal_state = [1,2,3,4,5,6,7,8,0]
        self.frontier = Q.PriorityQueue()
        self.explored = []
    
    
    def Solve(self):
        nodes_expanded = 0    
        nodes_queue = 0
        
        if(self.init_state.puzz_tiles == self.goal_state):              #if the inital state = goal state
            self.init_state.display()
            print "the search algorithm expanded a total of 0 nodes."
            print "the maximum number of nodes in the queue at any one time was 0"
            print "the depth of the goal node was 0"
            return
        
        next_states = self.init_state.check_move()
        nodes_expanded += 1                                             #increase count everytime we expand a node
        for i in next_states:
            self.frontier.put(i)                                        #next states have been added to the frontier
            
        if(self.frontier.qsize() > nodes_queue):
            nodes_queue = self.frontier.qsize()
        
        self.explored.append(self.init_state)                           #initial state is put into the explored list
        
        while not self.frontier.empty():                                #while the frontier is not empty
            top_state = self.frontier.get()
            
            if(top_state.puzz_tiles == self.goal_state):                 #if the state popped off = the goal state
                top_state.trace_path(self.init_state, nodes_expanded, nodes_queue)
                return
            
            in_explored = 0
            
            for i in range(len(self.explored)):                         #check to make sure the popped state hasnt been explored 
                if(top_state.puzz_tiles == self.explored[i].puzz_tiles):
                    in_explored = 1
                    break
                
            if(in_explored == 1):                                       #dont expand if the state has already been expanded
                continue
            
            next_states = []
            next_states = top_state.check_move()                        #stores all the next states, following the expanded state
            nodes_expanded += 1                                         #increase count everytime we expand a node

            for i in next_states:
                self.frontier.put(i)                                    #next states have been added to the frontier
            
            
            if(self.frontier.qsize() > nodes_queue):
                nodes_queue = self.frontier.qsize()
            
            
            self.explored.append(top_state)                             #initial state is put into the explored list
