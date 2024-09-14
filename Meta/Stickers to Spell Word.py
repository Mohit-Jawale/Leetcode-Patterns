class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:


        sticker_count = [Counter(sticker) for sticker in stickers]

        memo = {}

        
        def dfs(target_str):
            
            if len(target_str)==0:
                return 0
            
            if target_str in memo:
                return memo[target_str]
            
            target_counter = Counter(target_str)
            
            min_count = float('inf')

            for sticker_counter in sticker_count:
                
                if target_str[0] not in sticker_counter:
                    continue

                remaining_char = target_counter - sticker_counter
                letter = [char*count for char,count in remaining_char.items()]
                next_str = "".join(letter)
            
                min_count = min(dfs(next_str)+1,min_count)

            memo[target_str] = min_count
            
            return min_count
            
        ans = dfs(target) 
        return ans if ans != float('inf') else -1











        
