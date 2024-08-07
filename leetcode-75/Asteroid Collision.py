class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        i=0
        while i<len(asteroids):
            if stack and asteroids[i]<0:
                
                if stack[-1]<0 and asteroids[i]<0:
                    stack.append(asteroids[i])
                    i+=1
                elif stack[-1]>abs(asteroids[i]):
                    i+=1
                    continue
                elif stack[-1]<abs(asteroids[i]):
                    stack.pop()
                else:
                    stack.pop()
                    i+=1
            else:
                stack.append(asteroids[i])
                i+=1

        return stack

      
