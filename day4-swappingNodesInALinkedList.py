# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head, k):
        #         size,temp=1,head

        #         #get size
        #         while temp.next:
        #             size+=1
        #             temp=temp.next

        #         #get left_k value
        #         left_k=head
        #         for i in range(1,k):
        #             left_k=left_k.next

        #         #get right_k value and swap with left_k value
        #         right_k=head
        #         for i in range(1,size-k+1):
        #             right_k=right_k.next

        #         left_k.val,right_k.val=right_k.val,left_k.val
        #         return head

        #         #Another Method

        #         leftk=rightk=head

        #         #get value of left k
        #         for i in range(1,k):
        #             leftk=leftk.next

        #         #now we dont know right k as it needs to be travelled from right
        #         #and its not possible with singly linkd list
        #         #so we have to take pointer which is less than k of last node ie tail node
        #         #so we will take two nodes one for right k and other for tail node
        #         #untill tail.next is none we will move to right with both nodes
        #         #and as left k is already k moves ahead of head
        #         #(actually its k-1 moves as in k head position is already considered)
        #         #and we have to actually travel with one pointer(right k pointer) k-1 moves behind tail pointer
        #         #so right k will start from head and tail pointer will start from kth position ie left k
        #         #and when iterating upto when tail.next is None then right k will be at k position from right

        #         tail=leftk
        #         while tail.next:
        #             rightk, tail=rightk.next, tail.next
        #         #now swap the left k and right k values
        #         leftk.val,rightk.val=rightk.val,leftk.val
        #         return head

        # ANOTHER APPROACH

        # make a list of linked list nodes
        # now as in count of upto k th position means head is already present
        # so when moving from initialization as k, count would be k-1 ie left k would be arr[k-1]
        # and swap the node.val of arr[k-1] and arr[-k]

        # Runtime: 981 ms, faster than 99.98% of Python3 online submissions for Swapping Nodes in a Linked List.
        # Memory Usage: 48.4 MB, less than 57.29% of Python3 online submissions for Swapping Nodes in a Linked List.

        arr = []
        pointer = head
        while pointer:
            arr.append(pointer)
            pointer = pointer.next
        arr[k-1].val, arr[-k].val = arr[-k].val, arr[k-1].val
        return head
