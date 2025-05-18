class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        #### take the ladder for the greater heights later on using maxHEap
        #### if im not able to reach the index of the max heap I will pop


        #### Lazy Greedy solution

        max_heap = []

        for index in range(len(heights) - 1):
            diff = heights[index + 1] - heights[index]

            if diff <= 0:
                continue

            if bricks >= diff:
                heapq.heappush(max_heap, -diff)
                bricks -= diff
            else:
                if ladders > 0:
                    if max_heap and -max_heap[0] > diff:
                        # Replace largest previous brick use with ladder
                        max_bricks = -heapq.heappop(max_heap)
                        bricks += max_bricks  # refund
                        bricks -= diff        # use bricks for this diff
                        heapq.heappush(max_heap, -diff)
                    # else: just use ladder directly, no change in heap
                    ladders -= 1
                else:
                    return index

            if bricks < 0:
                return index

        return len(heights) - 1
                
                    
                    
                        






        # memo = {}
        # def dfs(i,curr_bricks,remaining_ladders):

        #     if i>=(len(heights)-1):
        #         return i

        #     key = (curr_bricks,remaining_ladders)

        #     if key in memo:
        #         return memo[key]
          
        #     max_reach = i
       
        #     if heights[i]>=heights[i+1]:
        #         memo[key] = dfs(i+1,curr_bricks,remaining_ladders)
        #         return memo[key]
        #     else:
                
        #         required_bricks_for_jump = (heights[i+1]-heights[i])

        #         if curr_bricks>=required_bricks_for_jump :
        #             max_reach = max(dfs(i+1,curr_bricks-required_bricks_for_jump,remaining_ladders),max_reach)

        #         if remaining_ladders>0:
        #             max_reach = max(dfs(i+1,curr_bricks,remaining_ladders-1),max_reach)

        #         memo[key] = max_reach
        #         return max_reach
         

        # return dfs(0,bricks,ladders)
            

                    



