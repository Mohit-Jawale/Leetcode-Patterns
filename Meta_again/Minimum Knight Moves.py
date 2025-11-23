class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:


        ### edge case: if x and y are same as start point
        if x==0 and y ==0 :
            return 0

        queue = collections.deque([[0,0,0]])

        moves = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        visited = {(0,0):0}


        while queue:

            i,j,curr_steps = queue.popleft()

            for ni,nj in moves:

                new_i,new_j = ni+i , nj+j

                if (new_i,new_j) in visited:
                    if visited[(new_i,new_j)]>curr_steps+1:
                        visited[(new_i,new_j)]=curr_steps+1


                if new_i == x and new_j == y:
                    return curr_steps+1
                
                if (new_i,new_j) not in visited:
                    queue.append([new_i,new_j,curr_steps+1])
                    visited[(new_i,new_j)] = curr_steps+1
        


        
