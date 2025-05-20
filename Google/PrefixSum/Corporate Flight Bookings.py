class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        diff_array = [0]*(n+2) #### here n+2 bcz indexing is from zero and will update last+1

        for start,end,seats in bookings:
            diff_array[start]+=seats
            diff_array[end+1]-=seats
        
    
        for index in range(1,n+1):
            diff_array[index] = diff_array[index-1]+diff_array[index]
        
        return diff_array[1:n+1]



        



        
