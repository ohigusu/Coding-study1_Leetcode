class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score,result=0,0
        stack = []

        for char in s:
            if char == "(": 
                stack.append(0)
            if char == ")":
                temp = stack.pop()
                if temp == 0:
                    score = 1
                    stack.append(score)
                    score = 0
                else:
                    while temp != 0:
                        score += temp
                        temp = stack.pop()
                    stack.append(2*score)
                    score = 0  
        while stack:
            result += stack.pop()
        return result
        
