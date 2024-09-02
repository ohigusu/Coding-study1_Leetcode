class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":return []
        letters = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        answer,dict = [],[]
        for i in digits:
            dict.append(letters[i])
        def dfs(visited,idx):
            if len(visited) == len(dict):
                answer.append(visited)
            else:
                for char in dict[idx]:
                    visited += char
                    dfs(visited,idx+1)
                    visited=visited[:-1]
        dfs("",0)
        return answer
        