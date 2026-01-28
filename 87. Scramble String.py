from collections import Counter

class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False

        memo = {}

        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            # Base case
            if a == b:
                memo[(a, b)] = True
                return True

            # Prune by character frequency
            if Counter(a) != Counter(b):
                memo[(a, b)] = False
                return False

            n = len(a)
            for i in range(1, n):
                # Case 1: no swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True

                # Case 2: swap
                if dfs(a[:i], b[n - i:]) and dfs(a[i:], b[:n - i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
