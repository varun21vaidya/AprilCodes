# https://leetcode.com/problems/convert-bst-to-greater-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # sum=0  #for recursive

    def convertBST(self, root):

        # Recursive Approach

        #         if (root==None): return None

        #         self.convertBST(root.right)   #first get to the rightmost element
        #         self.sum+=root.val            #then add the current nodes value to sum
        #         root.val=self.sum             #then update current node with sum
        #         self.convertBST(root.left)    #travese to check left nodes
        #         return root

        # Iterative Approach

        # Runtime: 69 ms, faster than 99.27% of Python3 online submissions for Convert BST to Greater Tree.
        # Memory Usage: 16.7 MB, less than 53.49% of Python3 online submissions for Convert BST to Greater Tree.

        lst = []
        curr = root
        sum = 0
        while lst or curr:
            while curr:
                lst.append(curr)
                curr = curr.right
            curr = lst.pop()
            sum += curr.val
            curr.val = sum
            curr = curr.left

        return root
