# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.search(root)


    def search(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left = self.search(root.left)
        right = self.search(root.right)

        if root.left == None:
            return 1 + right
        
        if root.right == None:
            return 1 + left
        
        return 1 + (right if right < left else left)