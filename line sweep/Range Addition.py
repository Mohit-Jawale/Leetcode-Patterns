class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        diff_arr = [0]*(length+1)

        for s,e,inc in updates:
            diff_arr[s]+=inc
            diff_arr[e+1]-=inc
        
        for i in range(1,length):
            diff_arr[i]+=diff_arr[i-1]
        
        return diff_arr[0:length]
        
