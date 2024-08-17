### here two sets are requireed unique and duplicate bcz we have to remember the state of duplicate consider example 1,1,1
class FirstUnique:

    def __init__(self, nums: List[int]):

        self.queue = []
        self.unique = set()
        self.duplicate = set()
        for num in nums:
            self.queue.append(num)
            if num not in self.duplicate:
                self.unique.add(num)
                self.duplicate.add(num)
            elif self.unique and  num in self.unique:
                    self.unique.remove(num)
        
    def showFirstUnique(self) -> int:
       
        while self.queue and self.queue[0] not in self.unique:
            self.queue.pop(0)
        return self.queue[0] if self.queue else -1

        

    def add(self, value: int) -> None:

        self.queue.append(value)
        if value not in self.duplicate:
            self.unique.add(value)
            self.duplicate.add(value)
         
        elif self.unique and  value in self.unique:
            self.unique.remove(value)

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
