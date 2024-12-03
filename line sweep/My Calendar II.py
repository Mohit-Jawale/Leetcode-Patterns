class MyCalendarTwo:

    def __init__(self):

        self.counter = collections.Counter()
        
    
    def book(self, startTime: int, endTime: int) -> bool:
        self.counter[startTime]+=1
        self.counter[endTime]-=1
        count = 0

        for time in sorted(self.counter.keys()):
            count+=self.counter[time]

            if count==3:
                self.counter[startTime]-=1
                self.counter[endTime]+=1
            
                return False

        return True
        



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)


