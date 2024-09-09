class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        hashmap = collections.defaultdict(list)
        ### rememeber upward i+j downward is i-j trick

        for i in range(len(mat)):
            for j  in range(len(mat[0])):

                hashmap[i+j].append(mat[i][j])
        
        ans = []

        for i in range(0,len(mat)+len(mat[0])-1):
            if i%2!=0:## odd
                ans+=hashmap[i]
            else:
                ans+=hashmap[i][::-1]
        return ans
            



        

        
