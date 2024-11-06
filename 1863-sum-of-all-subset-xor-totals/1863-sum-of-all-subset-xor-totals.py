class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def sums(term,idx):
            if idx == len(nums) : 
                return term
            return sums(term,idx+1) + sums(term ^ nums[idx],idx+1)
        return sums(0,0)
            
        
    

# 1 = 001,  2 = 010,   3 = 011,   4 = 100,   5 = 101,   6 = 110 , 7 = 111, 
# 8 = 1000   
#16 = 10000

