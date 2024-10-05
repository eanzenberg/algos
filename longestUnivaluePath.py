# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def longestUnivaluePath(root: Optional[TreeNode]) -> int:
    result = 0

    def dfs(node, parent):
        nonlocal result
        
        if node == None:
            return 0

        left = dfs(node.left, node)
        right = dfs(node.right, node)
        
        if left + right > result:
            result = left + right
        
        if parent and parent.val == node.val:
            return max(left, right) + 1
        return 0
    
    dfs(root, None)

    return result