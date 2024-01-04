def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_height = self.maxDepth(root.left)
    right_height = self.maxDepth(root.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1
