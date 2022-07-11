"""
Recursive Approach
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def utilInorderTraversal(self, root: Optional[TreeNode], res):
        if root == None:
            return
        if root.left != None:
            self.utilInorderTraversal(root.left, res)
        res.append(root.val)
        if root.right != None:
            self.utilInorderTraversal(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.utilInorderTraversal(root, res)
        return res
