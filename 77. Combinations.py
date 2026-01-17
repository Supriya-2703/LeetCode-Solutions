class Solution:
    def combine(self, n, k):
        res = []
        
        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
        
        backtrack(1, [])
        return res
