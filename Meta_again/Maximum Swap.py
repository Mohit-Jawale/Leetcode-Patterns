class Solution:
    def maximumSwap(self, num: int) -> int:


        #### find the largest number in the right and swap with smallest number in left

        if num<11:
            return num

        num_as_arr = collections.deque([])

        while num:
            num_as_arr.appendleft(num%10)
            num//=10
        
        max_seen = -1
        max_seen_at = len(num_as_arr)
        i = len(num_as_arr)-1

        while i>=0:

            curr_num = num_as_arr[i]

            num_as_arr[i] = (curr_num,max_seen_at,max_seen)

            if max_seen<curr_num:
                max_seen = curr_num
                max_seen_at = i
            
            i-=1
        
        i=0

        while i<len(num_as_arr):

            curr_num,max_seen_at, max_seen = num_as_arr[i]

            if curr_num<max_seen:
                num_as_arr[max_seen_at], num_as_arr[i] = num_as_arr[i],  num_as_arr[max_seen_at]
                break
            
            i+=1
        

        num = 0
        for curr_num,_,_ in num_as_arr:

            num = num*10 + curr_num
        
        return num

        
