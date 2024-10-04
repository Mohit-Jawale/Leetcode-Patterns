class Solution:
    def reversePairs(self, nums: List[int]) -> int:



        def mergeSort(start,end):

            if start>=end:
                return 0
            
            mid = (start+end)//2
            count = mergeSort(start,mid) +  mergeSort(mid+1,end)


            i = start
            j = mid+1

            while i<=mid and j<=end:

                if nums[i] > 2* nums[j]:
                    count+= mid - i + 1 ##counting the remaining elements
                    j+=1
                else:
                    i+=1
            
            nums[start:end+1] = sorted(nums[start:end+1])
            
            return count
        
        return mergeSort(0,len(nums)-1)





        
