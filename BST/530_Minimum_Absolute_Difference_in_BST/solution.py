# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def getMinimumDifference(root) -> int:
    min_absoulte_diff = 100000
    current = root
    stack = []
    prev = None

    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif stack:
            current = stack.pop()

            if prev is None:
                prev = current.val
            else:
                diff = abs(current.val - prev)
                if diff < min_absoulte_diff:
                    min_absoulte_diff = diff
                prev = current.val

            current = current.right

        else:
            break

    return min_absoulte_diff
