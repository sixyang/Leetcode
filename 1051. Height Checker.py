class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sheights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sheights[i]:
                count += 1
        return count
