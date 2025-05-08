class Solution:
    def partition(self, s: str) -> List[List[str]]:

        #### all solution we have to give so this is backtracking 
        ####  

    
        #### Time Complexity - : O(2^N*N) and Space Complexity - : O(N*2^N)

        ans = []

        def checkPalindrome(substring):

            if substring==substring[::-1]:
                return True
            return False


        def partitionString(i,palindrome_partition_list):


            if i==len(s):
                ans.append(palindrome_partition_list[:])
                return
            if i>len(s):
                return 
            
            
            for k in range(i,len(s)):

                if checkPalindrome(s[i:k+1]):
                    palindrome_partition_list.append(s[i:k+1])
                    partitionString(k+1,palindrome_partition_list)
                    palindrome_partition_list.pop()
        

        partitionString(0,[])

        return ans





          


            
        
