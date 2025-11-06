class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"

        term = "1"
        for _ in range(2, n + 1):
            res = []
            count = 1
            for i in range(1, len(term)):
                if term[i] == term[i - 1]:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(term[i - 1])
                    count = 1
            res.append(str(count))
            res.append(term[-1])
            term = "".join(res)

        return term
