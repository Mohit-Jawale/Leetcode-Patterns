class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        counter_2 = Counter(p)
        counter_1 = Counter(s[:len(p)])
        matches = 0

        for i in range(0,26):
            char = chr(ord('a')+i)
            if char not in counter_1:
                counter_1[char]=0
            if char not in counter_2:
                counter_2[char]=0 
            if counter_1[char]==counter_2[char]:
                matches+=1

        left, right = 0, len(p)
        ans = []

        while right<len(s):

            if matches == 26:
                ans.append(left)

            counter_1[s[right]]+=1
            if counter_1[s[right]]==counter_2[s[right]]:
                matches+=1
            elif counter_1[s[right]] == counter_2[s[right]]+1:
                matches-=1

            counter_1[s[left]]-=1
            if counter_1[s[left]]==counter_2[s[left]]:
                matches+=1
            elif counter_1[s[left]] == counter_2[s[left]]-1:
                matches-=1

            left+=1
            right+=1

        if matches == 26:
            ans.append(left)
        return ans            


