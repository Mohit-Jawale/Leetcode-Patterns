# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        ans = []
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n+=1


        eachpartition = n//k
        firstextrapartions = n%k
        remaining = (k-firstextrapartions)

        temp = head

    
        while firstextrapartions>0:
            partition = temp
            prev = None
            i=0
            while i<eachpartition+1:
                prev = temp
                temp=temp.next
                i+=1
            prev.next = None
            ans.append(partition)
            firstextrapartions-=1

        
        while remaining:
            i = 0
            partition = temp
            prev = None
            while temp and i<eachpartition:
                prev = temp
                temp=temp.next
                i+=1
            
            if prev:
                prev.next = None
            ans.append(partition)
            remaining-=1

        return ans
            
            




            
        
