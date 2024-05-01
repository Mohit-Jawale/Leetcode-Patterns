class RandomizedSet:

    def __init__(self):
        self.randomized_set = {}
        self.randomList = []
        

    def insert(self, val: int) -> bool:
        if val not in self.randomized_set:
            self.randomized_set[val] = len(self.randomList) 
            self.randomList.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.randomized_set:
            return False
        index = self.randomized_set[val]
        self.randomized_set[self.randomList[-1]] = index
        self.randomList[index] = self.randomList[-1]
        self.randomList.pop()
        del self.randomized_set[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.randomList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
