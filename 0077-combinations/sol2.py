class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        self.help(n, k, 1, [], result)
        return result


    def help(self, n, k, start_idx, curr_list, result):

        if len(curr_list) == k:
            result.append(curr_list[:])
            return

        for i in range(start_idx, n+1):
            curr_list.append(i)
            self.help(n, k, i+1, curr_list, result)
            curr_list.pop()
