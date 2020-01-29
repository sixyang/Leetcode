class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # import numpy as np
        # nums = np.zeros((n, m))
        # for i in indices:
        #     nums[i[0]] += 1
        #     nums[:, i[1]] += 1
        # return int(np.sum(nums % 2))
        nums = [[0 for j in range(m)] for i in range(n)]
        for i in indices:
            nums[i[0]] = [j+1 for j in nums[i[0]]]
            for k in range(len(nums)):
                nums[k][i[1]] += 1
        count = 0
        for i in nums:
            for j in i:
                if j & 1 == 1:
                    count += 1
        return count
