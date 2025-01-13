class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        #### very interesting BFS implementation

        queue = collections.deque([[id]])

        visited = set()
        curr_level = 0
        level_friends = []
        visited.add(id)

        while queue:

            curr_level+=1
         
            node_ids = queue.popleft()
            temp = set()

            for friend_id in node_ids:
                for friends_id in friends[friend_id]:
                    if friends_id not in visited:
                        temp.add(friends_id)
                        visited.add(friends_id)
            if temp:
                queue.append(temp)

            if curr_level == level:
                level_friends = temp
                break
            

        videos_freq = collections.Counter()


        for friend_id in level_friends:
            for video in watchedVideos[friend_id]:
                videos_freq[video]+=1

        sorted_items = sorted(videos_freq.items(), key=lambda x: (x[1], x[0]))
        ans = list(dict(sorted_items).keys())
        return ans
        




