class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()

        def dfs(i):

            if i in visited:
                return

            visited.add(i)

            for roomNo in rooms[i]:
                if roomNo not in visited:
                    dfs(roomNo)

        
        dfs(0)
        return True if len(visited)-1 == len(rooms)-1 else False
