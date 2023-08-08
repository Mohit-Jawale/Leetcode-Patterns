### This is the self implementation...go through it or implement again during revision
import heapq as hq
class Twitter:

    def __init__(self):

        self.time = 0
        self.maxHeap = [] 
        hq.heapify(self.maxHeap)
        self.connections = collections.defaultdict(list)
    

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        tweet = (-self.time,userId,tweetId)
        hq.heappush(self.maxHeap,tweet)
        
        
    def getNewsFeed(self, userId: int) -> List[int]:

        temp = []
        ans = []
        count = 0
    
        while len(self.maxHeap)!=0 and count<10:

            top = hq.heappop(self.maxHeap)
            if (self.connections.get(userId) and top[1] in self.connections[userId]) or top[1]==userId:
                ans.append(top[2])
                count+=1
            temp.append(top)

        [hq.heappush(self.maxHeap,tweet) for tweet in temp]   
    
        return ans            


    def follow(self, followerId: int, followeeId: int) -> None:
        self.connections[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
