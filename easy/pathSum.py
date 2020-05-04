# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """

    if root is None:
        return False

    def _hasPathSum(node, og_sum, sum=0):

        if node is None:
            if sum == og_sum:
                return True
            else:
                return False

        sumToPass = sum + node.val

        if _hasPathSum(node.left, og_sum, sumToPass):
            return True
        elif _hasPathSum(node.right, og_sum, sumToPass):
            return True
        else:
            return False


    return _hasPathSum(root, sum)

if __name__ == '__main__':
    pass
