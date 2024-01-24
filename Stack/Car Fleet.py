#### This problem has lot of things goings on best explaination is with neetcode if u forget the intuition.
### Just remember u have to sort it and the transever from behind by putting time in the stack and then comparing if top is smaller that then
#### the second top postion pop it.



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p,s] for p,s in zip(position,speed)]

        stack = []

        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:### this means if some car is reaching before top then they must have meet and become fleet before
                stack.pop()

        return len(stack)        
