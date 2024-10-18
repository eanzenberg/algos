from collections import defaultdict, deque
from typing import List


def verticalTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    mapped_nodes = defaultdict(list)

    queue = deque([(0, 0, root)]) # col row node

    min_col, max_col = 0, 0

    while queue:
        col, row, node = queue.popleft()

        min_col = min(min_col, col)
        max_col = max(max_col, col)

        mapped_nodes[col].append((row, node.val))

        if node.left:
            queue.append((col - 1, row - 1, node.left))

        if node.right:
            queue.append((col + 1, row - 1, node.right))

    ans = []

    print(mapped_nodes)

    for i in range(min_col, max_col + 1):
        sorted_nodes = sorted(mapped_nodes[i], key=lambda t: (-t[0], t[1]))
        ans.append([y for _, y in sorted_nodes])
    
    return ans