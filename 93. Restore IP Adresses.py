class Solution:
    def restoreIpAddresses(self, s):
        res = []
        
        def backtrack(index, parts, path):
            # If 4 parts are formed and all digits are used
            if parts == 4 and index == len(s):
                res.append(".".join(path))
                return
            
            # If too many parts or ran out of digits
            if parts == 4 or index == len(s):
                return
            
            # Try segment lengths 1 to 3
            for length in range(1, 4):
                if index + length > len(s):
                    break
                
                part = s[index:index + length]
                
                # Leading zero check
                if part[0] == '0' and length > 1:
                    continue
                
                # Value check
                if int(part) <= 255:
                    backtrack(index + length, parts + 1, path + [part])
        
        backtrack(0, 0, [])
        return res
