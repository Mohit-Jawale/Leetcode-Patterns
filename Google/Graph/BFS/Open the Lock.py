###https://leetcode.com/problems/open-the-lock/
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        ### min total no === bfs
        #### start and target is given can try bidirectional bfs
        #### there are obstacles too

        queue = collections.deque([("0000",0)])

        target_list = list(target)

        visited = set()

        deadends = set(deadends)

        while queue:

            currNode,currSteps = queue.popleft()


            if  currNode == target:
                return currSteps

            if  currNode in deadends:
                continue

            if currNode in visited:
                continue
            
            visited.add(currNode)


            for i in range(4):
                
                digit = int(currNode[i])

                for dir in [-1,1]:
                    newDigit = (digit+dir)%10
                    newStr = currNode[:i]+str(newDigit)+currNode[i+1:]

                    if newStr not in visited:
                        queue.append((newStr,currSteps+1))

        return -1

                 







        
