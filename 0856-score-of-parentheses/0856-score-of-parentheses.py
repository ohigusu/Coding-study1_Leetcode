
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        summ = 0
        multiplier = 1
        stack = []
        for elem in s:
            if elem == ')':
                while stack[-1] != '(':
                    summ += stack.pop()
                    multiplier = 2
                if not summ:
                    summ = 1
                stack.pop()
                stack.append(summ*multiplier)
                multiplier = 1
                summ = 0
            else:
                stack.append(elem)
        sol = 0 
        while stack:
            sol += stack.pop()
        return sol

        