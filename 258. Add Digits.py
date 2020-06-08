class Solution:
    def addDigits(self, num: int) -> int:
        # Near！
        # while True:                   # 这是我自己写的，虽然思路非常简单。但是不满足题意
        #     num_str = str(num)
        #     if len(num_str) == 1: return int(num_str)
        #     temp_num = 0
        #     for i in num_str:
        #         temp_num += int(i)
        #     num = temp_num

        if num > 9:                     # 这实在是太强了！
            num %= 9
            if not num: return 9
        return num
            
