class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # 中等题？ 就这？ 一开始还以为有什么玄机，然后把测试案例都过了一遍都萌大奶，emmm
        pos = []
        for i in range(len(nums)):
            if nums[i] == 1: pos.append(i)
        for j in range(1, len(pos)):
            if pos[j] - pos[j-1] <= k: return False
        return True
