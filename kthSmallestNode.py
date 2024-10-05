# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    vals = set()

    def dfs(node):
        nonlocal vals

        if not node:
            return
        
        left = dfs(node.left)
        right = dfs(node.right)

        vals.add(node.val)

        return node.val
    
    dfs(root)
    print(vals)

    return sorted(list(vals))[k-1]