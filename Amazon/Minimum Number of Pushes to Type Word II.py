class Solution:
    def minimumPushes(self, word: str) -> int:

        counter = Counter(word)
        ans = 0
        levelcnt = 0
        for letter,count in counter.most_common():

            if levelcnt<8:
                ans = ans + (count)
                levelcnt+=1
            elif levelcnt>=8 and levelcnt<16:
                ans = ans + (count*2)
                levelcnt+=1
            elif levelcnt>=16 and levelcnt<24:
                ans = ans+(count*3)
                levelcnt+=1
            else:
                ans = ans+(count*4)
                levelcnt+=1


        return ans

        
