class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in nums:                      # 这竟然没有超时，emmmm，不过执行时间 5028，也是够呛~
        #     if nums.count(i) > 1:return i

        # 这是直接抄的力扣官方题解，题解给的前两个解法在约束条件下根本不成立，所以这种解法也只能去抄了~
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1
