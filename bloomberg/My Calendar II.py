class MyCalendarTwo:

    def __init__(self):

        self.CalenderEvents = []


    
    def book(self, startTime: int, endTime: int) -> bool:

        self.CalenderEvents.append((startTime,+1))
        self.CalenderEvents.append((endTime,-1))

        self.CalenderEvents.sort(key = lambda x: (x[0],x[1]))

        active_booking = 0

        for time,event_type in  self.CalenderEvents:
            if event_type==1:
                active_booking+=1
            else:
                active_booking-=1
   
            if active_booking>=3:
                self.CalenderEvents.remove((startTime, +1))
                self.CalenderEvents.remove((endTime, -1))
                return False
        
        return True



        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
