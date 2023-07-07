class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        monotonic_stack = []

        for i in range(len(temperatures)):
            if not monotonic_stack:
                monotonic_stack.append((temperatures[i],i))
            else:
                while monotonic_stack and temperatures[i]>monotonic_stack[-1][0] :
                    ans[monotonic_stack[-1][1]]= i-monotonic_stack[-1][1]
                    monotonic_stack.pop()
                monotonic_stack.append((temperatures[i],i))   

        return ans        
