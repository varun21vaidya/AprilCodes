# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(root, k) -> int:

        # A brute force Approach:

        # first create a container to store the bst values
        # then using any traversal here inorder, append bst values to list
        # get the kth lowest element

        # TC: O(N) (due to sorting)
        # SC: O(N) (due to list creation)
        arr = []

        def helper(root, arr):
            if root:
                if root.left:
                    helper(root.left, arr)
                arr.append(root.val)
                if root.right:
                    helper(root.right, arr)

        helper(root, arr)
        return (arr)[k-1]

        # Instead of using array we use a count
        # assign it with k and decrease it till it reaches 0
        # and instead of returning directly assign a result and then return the result later

        self.res = None
        self.count = k

        def helper(root):
            if root.left:
                helper(root.left)
            self.count -= 1
            if self.count == 0:
                self.res = root.val
                return
            if root.right:
                helper(root.right)

        helper(root)
        return self.res
