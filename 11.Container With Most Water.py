# class Solution:
#     '''
#     基于双指针，降低复杂度。代码来自于Knife、的美化。
#     '''
#     def maxArea(self, height) -> int:
#         res, l, r = 0, 0, len(height) - 1               #l是从前往后的指针，r是从后往前的指针。res是结果。
#         while l < r:                                    #当两个指针没有相遇。
#             if height[l] < height[r]:                   #根据木桶效应，找小的那个值。
#                 res, l, r = max(res,  height[l] * (r - l)), l + 1, r #左侧右移
#             else: 
#                 res, l, r = max(res,  height[r] * (r - l)), l, r - 1 #右侧左移
#         return res
    
    '''
    没有系统的学过相关算法，对于双指针还不太熟悉。所以代码复杂度比较高，超出了时间限制，然后看了别人的一些答案，使用双指针实现了。总之，又学会了一些东西。等考试结束了把Leetcode上面的基本算法先全部看一遍吧！
    '''

'''
以下是自己的一开始做的结果，复杂度很高。
class Solution():
    def maxArea(self,li) -> int:
    max_v = 0
    li = [1,8,6,2,5,4,8,3,7]
    for index,i in enumerate(li):
        for index2,j in enumerate(li[index+1:]):        #这里index2的值并不是对应数字的真正索引！
            index2 += index
            v = abs(index2 - index + 1) * min(i,j)
            print(v)
            if v > max_v:
                max_v = v
    return (max_v)

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2020.4.18前来挑战~
        # 不知道怎的，就通过了……虽然我也是这个想法，但是没法确定这个算法的正确性，所以尝试性的写了一下，竟然还过了，emmmm……
        # 看完解析，已经知道这样正确性的原理了~
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            temp_area = (right-left)*min(height[left], height[right])
            if temp_area > max_area:
                max_area = temp_area
            if height[left] > height[right]: right -= 1
            else: left += 1
        return max_area
