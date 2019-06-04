class Solution:
    def reverse(self, x):
        flag = 0
        if x < 0:
            flag = 1
        x = str(abs(x))
        reverse_x = x[::-1]
        int_x = int(reverse_x)
        print(int_x)
        if int_x < -2**31 or int_x > 2**31-1:
            return 0
        elif flag:
            return -int_x
        else:
            return int_x
# solution = Solution()
# a = solution.reverse(-321)
# print(a)