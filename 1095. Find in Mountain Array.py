# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # 这题做起来思路还是蛮清晰的，为啥难度是hard，emmmm~
        left, right = 0, mountain_arr.length()-1
        while left < right:
            middle = (left + right) // 2
            if mountain_arr.get(middle+1) < mountain_arr.get(middle):
                right = middle
            else:
                left = middle + 1
        summit = left           # 找到峰顶~
        
        left, right = 0, summit
        while left < right:
            middle = (left + right) // 2
            if mountain_arr.get(middle) < target:
                left = middle + 1
            else:
                right = middle
        if mountain_arr.get(left) == target: return left

        left, right = summit, mountain_arr.length()-1
        while left < right:
            middle = (left + right) // 2
            if mountain_arr.get(middle) <= target:
                right = middle
            else:
                left = middle + 1
        if mountain_arr.get(left) == target: return left
        
        return -1   
