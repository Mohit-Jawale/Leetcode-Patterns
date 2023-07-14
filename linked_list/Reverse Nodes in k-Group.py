### This is really a complex problem dont starch ur head around it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def get_kth_node(curr,k):
            while curr and k>0:
                curr = curr.next
                k-=1
            return curr

        dummy_node = ListNode(-1,head)
        grp_head = dummy_node

        while True:
            kth_node  = get_kth_node(grp_head,k)  

            if kth_node == None:
                break

            curr,prev = grp_head.next, kth_node.next
            grp_next = kth_node.next

            while curr != grp_next:
                Next = curr.next
                curr.next = prev
                prev = curr
                curr = Next

            temp = grp_head.next
            grp_head.next = kth_node
            grp_head = temp
        return dummy_node.next       
