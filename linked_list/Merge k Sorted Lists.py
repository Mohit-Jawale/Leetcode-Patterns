####Imp is you remeber how to solve merge two list then use that to merge the k list




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge_two_list(l1,l2):

            node  = ListNode(-1)
            new_node = node

            while l1 and l2:

                if l1.val <= l2.val:
                    new_node.next = l1
                    l1 = l1.next
                else:
                    new_node.next = l2
                    l2 = l2.next

                new_node = new_node.next

            while l1:
                new_node.next = l1
                l1,new_node = l1.next,new_node.next

            while l2:
                new_node.next = l2
                l2,new_node = l2.next,new_node.next

            return node.next

        
        if len(lists)==0:
            return None

        
        while len(lists)>1:

            merged_list = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                merged_list.append(merge_two_list(l1,l2))
            lists = merged_list   

        return lists[0]

            
