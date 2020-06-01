class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 这才是六一应该做的题目吗？爱了爱了！ 六一快乐呀！
        most_candies = max(candies)
        ret = []
        for i in candies:
            if i + extraCandies >= most_candies: ret.append(True)
            else: ret.append(False)
        return ret
