class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def two_sum(target,i):

            left,right = i+1,len(nums)-1
            ans = set()

            while left<right:
                if (nums[left]+nums[right])<target:
                    left+=1
                elif(nums[left]+nums[right])>target:
                    right-=1
                else:
                    ans.add((i,left,right))
                    left+=1
                    right-=1

            return ans            


        nums.sort()
        res = []

        for index,num in enumerate(nums):
            
            ans = two_sum(-nums[index],index)
            if ans:
                for j in ans:
                    temp = (nums[j[0]],nums[j[1]],nums[j[2]])
                    if temp not in res :
                        res.append(temp)

        return list(res)            
