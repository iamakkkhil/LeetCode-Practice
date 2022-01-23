def rangeSumBST(self, root, low: int, high: int) -> int:
    def dfs(node):
        if node:
            if low <= node.val <= high:
                self.ans += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

    self.ans = 0
    dfs(root)
    return self.ans


if __name__ == "__main__":
    root = [10, 5, 15, 3, 7, None, 18]
    low = 7
    high = 15
    rangeSumBST(root, low, high)
