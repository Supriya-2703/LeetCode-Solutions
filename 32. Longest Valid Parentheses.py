class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]     
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()                
                if not stack:              
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses("(()"))     
    print(sol.longestValidParentheses(")()())"))  
    print(sol.longestValidParentheses(""))        
