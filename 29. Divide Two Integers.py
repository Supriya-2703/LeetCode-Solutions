class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        if dividend == INT_MIN and divisor == 1:
            return INT_MIN

        negative = (dividend < 0) != (divisor < 0)

        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        quotient = 0

        while dividend_abs >= divisor_abs:
            temp = divisor_abs
            multiple = 1
            while dividend_abs >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend_abs -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX

        return quotient


solution = Solution()

print(solution.divide(10, 3))   
print(solution.divide(7, -3))   
