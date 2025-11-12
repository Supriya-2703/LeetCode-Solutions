class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()          
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                val = candidates[i]
                if total + val > target:
                    break
                path.append(val)
                backtrack(i, path, total + val)  # can reuse same element
                path.pop()

        backtrack(0, [], 0)
        return res

if __name__ == "__main__":
    print(Solution().combinationSum([2,3,6,7], 7))  # [[2,2,3], [7]]
    print(Solution().combinationSum([2,3,5], 8))    # [[2,2,2,2],[2,3,3],[3,5]]
