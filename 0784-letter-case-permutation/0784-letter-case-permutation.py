class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def fun(sub="",i=0):
            if len(sub)==len(S):
                res.append(sub)
            else:
                if s[i].isalpha():
                    fun(sub+S[i],i+1)
                    fun(sub+S[i].swapcase(),i+1)
                else:fun(sub+S[i],i+1)
        res=[]
        fun()
        return res
        
                        


