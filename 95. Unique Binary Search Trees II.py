class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        memo = {}

        def build(start, end):
            if start > end:
                return [None]

            if (start, end) in memo:
                return memo[(start, end)]

            res = []
            for rootVal in range(start, end + 1):
                leftTrees = build(start, rootVal - 1)
                rightTrees = build(rootVal + 1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(rootVal)
                        root.left = l
                        root.right = r
                        res.append(root)

            memo[(start, end)] = res
            return res

        return build(1, n)
