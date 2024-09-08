class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def back(start,end,visited):
            if (end == n): 
                answer.append(visited[:])
                return 
            if start >= end+1:
                back(start,end+1,visited+")")
            if start < n:
                back(start+1,end,visited+"(")
        back(0,0,"")
        return answer





        
        