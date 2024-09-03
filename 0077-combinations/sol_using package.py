#sol1_using package
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        list_n = [i for i in range(1,n+1)]
        print(list_n)
        combos = combinations(list_n, k)
        return combos

#sol2_using package
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations(range(1, n+1), k)
