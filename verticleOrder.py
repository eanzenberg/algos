# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import deque, defaultdict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        mapped_nodes = defaultdict(list) # (row, prior_direction, node.val)

        queue = deque([(0, 0, None, root)]) # (column, row, prior_direction, node)

        min_col, max_col = 0, 0

        while queue:
            col, row, prior_direction, node = queue.popleft()

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            mapped_nodes[col].append((row, prior_direction, node.val))

            if node.left:
                queue.append((col - 1, row - 1, 'l', node.left))

            if node.right:
                queue.append((col + 1, row - 1, 'r', node.right))

        ans = []

        for i in range(min_col, max_col + 1):
            ans.append([tup[2] for tup in mapped_nodes[i]])

        return ans