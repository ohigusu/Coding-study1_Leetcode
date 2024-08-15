class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for c in s:
            if c == ")":
                    if stack[-1] == "(":
                        stack[-1] = 1
                    else:
                        num = 0
                        while stack and isinstance(stack[-1], int):
                            num += stack[-1]
                            stack.pop()
                        
                        if stack and stack[-1] == "(":
                            stack.pop()

                        stack.append(2 * num)
            else:
                stack.append(c)

        return sum(stack)
