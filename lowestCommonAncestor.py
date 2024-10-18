def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None

    if root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left is not None and right is not None:
        return root
    
    else:
        return left if left is not None else right