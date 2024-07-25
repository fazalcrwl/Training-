
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next








def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        lsit1=linked_list_to_list(list1)
        lsit2=linked_list_to_list(list2)  

        list3=lsit1+lsit2
        list3=sorted(list3)
        list3=create_linked_list(list3)
        return list3