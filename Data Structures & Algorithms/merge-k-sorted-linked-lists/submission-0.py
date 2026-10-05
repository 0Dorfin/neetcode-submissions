# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            while len(lists) > 1:
                merged_lists = []
                for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    if i + 1 < len(lists):
                        l2 = lists[i + 1]
                    else:
                        l2 = None
                    merged_lists.append(self.mergeLists(l1, l2))
                lists = merged_lists
            return lists[0]
        
    def mergeLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next