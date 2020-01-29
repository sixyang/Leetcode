class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        import numpy as np
        nums = np.zeros((n, m))
        for i in indices:
            nums[i[0]] += 1
            nums[:, i[1]] += 1
        return int(np.sum(nums % 2))
