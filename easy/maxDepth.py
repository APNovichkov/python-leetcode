# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    return getMaxDepth(root, 0)

def getMaxDepth(node, maxDepth):
    if node is None:
        return maxDepth

    maxDepth += 1
    leftMaxDepth = maxDepth
    rightMaxDepth = maxDepth

    if node.left is not None:
        leftMaxDepth = getMaxDepth(node.left, maxDepth)

    if node.right is not None:
        rightMaxDepth = getMaxDepth(node.right, maxDepth)

    return max(rightMaxDepth, leftMaxDepth)


if __name__ == '__main__':
    # Base case: - Should return 0
    root = None
    print(f'Max Depth: {maxDepth(root)}')

    # Test case 1: - Should return 4
    root = TreeNode('4')
    root.left = TreeNode('3')
    root.right = TreeNode('7')
    root.right.left = TreeNode('2')
    root.right.right = TreeNode('10')
    root.right.right.right = TreeNode('20')
    print(f'Max Depth: {maxDepth(root)}')

    # Test case 2: - Should return 3
    root = TreeNode('4')
    root.left = TreeNode('3')
    root.right = TreeNode('7')
    root.right.left = TreeNode('2')
    root.right.right = TreeNode('10')
    print(f'Max Depth: {maxDepth(root)}')
