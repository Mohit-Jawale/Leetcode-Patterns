class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        left,right = 0,0
        ans=0
        uniqueChar = defaultdict(int)

        while right<len(s):
            uniqueChar[s[right]]+=1
            while len(uniqueChar)>k:
                uniqueChar[s[left]]-=1
                if uniqueChar[s[left]]==0:
                    del uniqueChar[s[left]]
                left+=1

            ans = max(right-left+1,ans)
            right+=1

        return ans        
