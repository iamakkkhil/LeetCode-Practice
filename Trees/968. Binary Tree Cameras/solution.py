def minCameraCover(root) -> int:
    camCount = 0
    covered = {None}

    def dfs(root, parent=None, camCount=0):
        if root:
            dfs(root.left, root, camCount)
            dfs(root.right, root, camCount)

            if (
                parent is None
                and root not in covered
                or root.left not in covered
                or root.right not in covered
            ):
                camCount += 1
                covered.update({root, parent, root.left, root.right})

    dfs(root, None, camCount)
    return camCount


if __name__ == "__main__":
    root = [0, 0, None, 0, 0]
    minCameraCover(root)
