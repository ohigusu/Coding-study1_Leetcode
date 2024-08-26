class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        answer = [""]
        
        for i in range(len(S)):
            temp = []
            for j in range(len(answer)):
                if S[i].isalpha():
                    temp.append(answer[j] + S[i].lower())
                    temp.append(answer[j] + S[i].upper())
                else:
                    temp.append(answer[j] + S[i])
                    
            answer = temp
            
        return answer
                        


