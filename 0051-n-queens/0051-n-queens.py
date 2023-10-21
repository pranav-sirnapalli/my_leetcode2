class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
    
    def is_valid_state(self, state, n):
        return len(state) == n
    

    def get_candidate(self, state, n):
        if(not state):
            return range(n)    # queen can be placed anywhere we want if list is empty
        # find next position to populate
        position = len(state)
        candidates = set(range(n))
        # prune down candidates that place queen into attacks
        for row, col in enumerate(state):
            # discard column index if it is occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagnols
            candidates.discard(col+dist)
            candidates.discard(col-dist)
        return candidates
    
    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return
        
        for candidates in self.get_candidate(state, n):
            #recurse
            state.append(candidates)
            self.search(state, solutions, n)
            state.pop()
    
    def state_to_string(self, state, n):
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n-i-1)
            ret.append(string)
        return ret




    
