# https://leetcode.com/submissions/detail/155006490/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        if(root.left == None and root.right == None):
            return 1
        if(root.left != None and root.right == None):
            return self.minDepth(root.left) + 1
        elif(root.left == None and root.right != None):
            return self.minDepth(root.right) + 1
        lh = self.minDepth(root.left)
        rh = self.minDepth(root.right)
        return rh + 1 if(lh > rh) else lh + 1
