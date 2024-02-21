class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(list)
        
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        self.timestamp[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        
        longest_char = "".join(['z']*101)
        index = bisect_right(self.timestamp[key],[timestamp,longest_char])
        ### to avoid upper bound 
        if index<=0:
            return ""
        return self.timestamp[key][index-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# class TimeMap:

#     def __init__(self):
#         self.lookup = collections.defaultdict(list)
        
#     def binary_search(self,left,right,target,key):
#         ans = ""
#         while left<=right:
#             middle = (left+right)//2
#             #### if target is target the midddle than atleast middle is the value we want
#             if self.lookup[key][middle][0]<=target:
#                 ans = self.lookup[key][middle][1]
#                 left = middle+1
#             else:
#                 right = middle-1
                
#         return  ans                 



#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.lookup[key].append((timestamp,value))
    

#     def get(self, key: str, timestamp: int) -> str:
   

#         if not self.lookup.get(key):
#             return ""
#         else:
            
#              value = self.binary_search(0,len(self.lookup[key])-1,timestamp,key)
      
#              return value   
        


# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)
