# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.stack = []

    def inorder(self, root):
        if not root:
            return True
        left = self.inorder(root.left)
        self.stack.append(root.val) 
        right = self.inorder(root.right)
        

        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inorder(root)
        
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i] <= self.stack[i-1]:
                return False
        return True