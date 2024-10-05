# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
    vals = set()

    def dfs(node):
        nonlocal vals

        if not node:
            return -10
        
        left = dfs(node.left)
        right = dfs(node.right)

        vals.add(left)
        vals.add(right)

        return node.val

    dfs(root)
    print(vals)

    if len(list(vals)) < 3:
        return -1
    else:
        return sorted(list(vals))[2]