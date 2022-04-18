# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = TreeNode(val)
        if not self.root:
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if currNode.val > val:
                    if not currNode.left:
                        currNode.left = newNode
                        return
                    else:
                        currNode = currNode.left
                else:
                    if not currNode.right:
                        currNode.right = newNode
                        return
                    else:
                        currNode = currNode.right

    # put your leetcode here:
    #def kthSmallest(self, root,k): ...


def print2DUtil(root, space):

    COUNT = 5
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT, space):
        print(end=" ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)

# Wrapper over print2DUtil()


def print2D(root):

    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


node = [5, 3, 6, 2, 4, 1]
tn = Solution()
for i in node:
    tn.insert(i)
print2D(tn.root)

# print your result with leetcode function:

# print(tn.kthSmallest(tn.root,k))
