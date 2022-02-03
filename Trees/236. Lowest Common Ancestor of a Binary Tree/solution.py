class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def tree(current_node):
            if current_node == None:
                return False

            left = tree(current_node.left)
            right = tree(current_node.right)

            mid = current_node == p or current_node == q

            if left + right + mid >= 2:
                self.ans = current_node

            return mid or left or right

        tree(root)
        return self.ans
