class SeatManager:

    def __init__(self, n: int):
   
        self.minHeap = self.addSeats(n)
        self.reservedSeats = set()
        
    def addSeats(self,n):
        return [i for i in range(1,n+1)]
    def reserve(self) -> int:
        seat = heapq.heappop(self.minHeap)
        self.reservedSeats.add(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self.reservedSeats:a
            heapq.heappush(self.minHeap,seatNumber)
            self.reservedSeats.remove(seatNumber)
            

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
